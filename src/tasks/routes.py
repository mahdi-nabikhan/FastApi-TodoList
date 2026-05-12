from fastapi import APIRouter,Path,Depends,HTTPException
from tasks.models import *
from fastapi.responses import JSONResponse
from tasks.schemas import *
from sqlalchemy.orm import Session
router = APIRouter(tags=['task router'])
from core.database import get_db
from typing import List


@router.get('/tasks/', response_model=List[TaskResponseSchemas])
def get_all_tasks(db:Session=Depends(get_db)):
    tasks =  db.query(TaskModels).all()
    return tasks


@router.post('/task/create')
def create_task(request:TaskCreateSchemas,db:Session=Depends(get_db)):
    task=TaskModels(**request.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.put('/task/{id}',response_model=TaskResponseSchemas)
def update_task(request:TaskCreateSchemas,id:int,db:Session=Depends(get_db)):
    tasks = db.query(TaskModels).filter_by(id= id).first()
    if not tasks:
        raise HTTPException(status_code=404,detail='Task not found')
    
    
    for field,value in request.model_dump(exclude_unset=True).items():
        setattr(tasks,field,value)


@router.get('/task/detail/{id}',response_model=TaskResponseSchemas)
def detail_task(id:int,db:Session=Depends(get_db)):
    tasks = db.query(TaskModels).filter_by(id=id).first()
    if not tasks:
        raise HTTPException(status_code=404,detail='Task not found')
    return tasks


@router.delete('/delete/task/{id}',response_model=TaskResponseSchemas)
def delete_task(id:int,db:Session=Depends(get_db)):
    tasks = db.query(TaskModels).filter_by(id=id).first()
    if not tasks:
        raise HTTPException(status_code=404,detail='Task not found')
    db.delete(tasks)
    db.commit()
    return JSONResponse(status_code=200,content='Task remove Successfully')