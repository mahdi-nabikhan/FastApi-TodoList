from fastapi import APIRouter
router = APIRouter(tags=['task router'])


@router.get('/tasks/')
def hello_world():
    return {"massage":'hello world'}