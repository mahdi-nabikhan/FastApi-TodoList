from fastapi import FastAPI


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
