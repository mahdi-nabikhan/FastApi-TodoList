from fastapi import APIRouter,Path,Depends,HTTPException,Query,status
from users.models import *
from fastapi.responses import JSONResponse
from users.schemas import *
from sqlalchemy.orm import Session

from core.database import get_db
from typing import List
router = APIRouter(tags=['users router'])


@router.post('/login')
async def user_login(request:UserLoginSchemas,db:Session=Depends(get_db)):
    return {}

@router.post('/register')
async def user_register(request:UserRegisterSchemas,db:Session=Depends(get_db)):
    if db.query(UserModel).filter_by(username=request.username).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='username already exist')
    user_obj=UserModel(username=request.username)
    user_obj.set_password(request.password)
    db.add(user_obj)
    db.commit()
   
    return JSONResponse(content='user registerd successfully')



