from fastapi import FastAPI
import random

app = FastAPI()

name_list = [
    {'id':1,'name':'mmd'},
    {'id':2,'name':'ali'},
    {'id':3,'name':'amir'},
    {'id':4,'name':'mosen'},
    {'id':5,'name':'meti'},
]

@app.get('/')
def root():
    return {'massage':" Hello World! "}

@app.get('/names')
def retrieve_names_list():
    return name_list


@app.get('/name/{id}')
def retrive_name_detail(id:int):
    for name in name_list:
        if name['id'] == id:
            return name
        
        
@app.post('/name/create')
def create_user(name):
    user={'id':random.randint(6,100),'name':name}
    name_list.append(user)
    return {'message':'user successfully added'}


    