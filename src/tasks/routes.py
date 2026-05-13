from fastapi import APIRouter,Path,Depends,HTTPException,Query
from tasks.models import *
from fastapi.responses import JSONResponse
from tasks.schemas import *
from sqlalchemy.orm import Session
router = APIRouter(tags=['task router'])
from core.database import get_db
from typing import List


@router.get('/tasks/', response_model=List[TaskResponseSchemas])
def get_all_tasks(db:Session=Depends(get_db),
                  completed : bool = Query(None,description='filter tasks  based on being completed or not '),
                  limit:int=Query(gt=0,le=50,description='limiting the count of task to retrive'),
                  offset:int=Query(ge=0,deprecated='user for pagination base on passed item')):
    query =  db.query(TaskModel)
    if completed is not None:
        query.filter_by( is_complated = completed)
        return query 
    tasks=query.limit(limit).offset(offset).all()
    return query


@router.post('/task/create')
def create_task(request:TaskCreateSchemas,db:Session=Depends(get_db)):
    task=TaskModel(**request.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.put('/task/{id}',response_model=TaskResponseSchemas)
def update_task(request:TaskCreateSchemas,id:int,db:Session=Depends(get_db)):
    tasks = db.query(TaskModel).filter_by(id= id).first()
    if not tasks:
        raise HTTPException(status_code=404,detail='Task not found')
    
    
    for field,value in request.model_dump(exclude_unset=True).items():
        setattr(tasks,field,value)


@router.get('/task/detail/{id}',response_model=TaskResponseSchemas)
def detail_task(id:int,db:Session=Depends(get_db)):
    tasks = db.query(TaskModel).filter_by(id=id).first()
    if not tasks:
        raise HTTPException(status_code=404,detail='Task not found')
    return tasks


@router.delete('/delete/task/{id}',response_model=TaskResponseSchemas)
def delete_task(id:int,db:Session=Depends(get_db)):
    tasks = db.query(TaskModel).filter_by(id=id).first()
    if not tasks:
        raise HTTPException(status_code=404,detail='Task not found')
    db.delete(tasks)
    db.commit()
    return JSONResponse(status_code=200,content='Task remove Successfully')