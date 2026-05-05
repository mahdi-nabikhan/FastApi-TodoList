from fastapi import FastAPI,Query,status,HTTPException,Path,Form,Body,UploadFile,File
from fastapi.responses import JSONResponse
import random
from dataclasses import dataclass
from schemas import *
from typing  import Annotated,List
from fastapi_swagger import patch_fastapi
app = FastAPI(docs_url=None,swagger_ui_oauth2_redirect_url=None)
patch_fastapi(app=app,docs_url='/swagger')
name_list = [
    {'id':1,'name':'mmd'},
    {'id':2,'name':'ali'},
    {'id':3,'name':'amir'},
    {'id':4,'name':'mosen'},
    {'id':5,'name':'meti'},
]

    
@app.get('/')
def root():
    return JSONResponse(content={'message':'hello world'},status_code=status.HTTP_200_OK)

@app.get('/names',status_code=status.HTTP_200_OK,response_model=List[PresonResponseSchema])
def retrieve_names_list():
    return name_list


@app.get('/name/{id}',status_code=status.HTTP_200_OK,response_model=PresonResponseSchema)
def retrive_name_detail(id:int=Path(title='object id',description='id of name in')):
    for name in name_list:
        if name['id'] == id:
            return JSONResponse(content={'message':name},status_code=status.HTTP_200_OK)
        
        
@app.post('/name/create',status_code=status.HTTP_201_CREATED,response_model=PresonResponseSchema)
def create_user(student : PersonCreateSchema):
    user={'id':random.randint(6,100),'name':student.name,'age':student.age}
    name_list.append(user)
    return user


    
@app.put('/names/{id}',status_code=status.HTTP_201_CREATED,response_model=PrsonUpdateSchema)
def update_name(name:PrsonUpdateSchema,id:int=Path(title='object id',description='id of name in name')):
    for item in name_list:
        if item["id"] == id :
            print(item)
            item["name"] = name.name
            return JSONResponse(content={'message':item},status_code=status.HTTP_201_CREATED)
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='name not found')



@app.delete('/delete/name/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_name(id:int=Path(title='object id',description='id of name in name')):
    for item in name_list:
        if item['id'] == id:
            name_list.remove(item)
        return JSONResponse(content={'message':'object delete successfully'},status_code=status.HTTP_201_CREATED)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    
@app.get('/search/name',status_code=status.HTTP_200_OK)
def search_names (q:str |None=Query(max_length=10)):
    if q:
        return JSONResponse(content={'message':[item for item in name_list if item['name'] == q]},status_code=status.HTTP_201_CREATED)
        
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='name not found')
    
    
    
    
@app.post('/upload/file')
async def upload_file(file:UploadFile=File(...)):
    content= await file.read()
    return {'filename':file.filename,'content_type':file.content_type,'file_size':len(content)}
    