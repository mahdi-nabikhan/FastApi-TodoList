from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPBasic,HTTPBasicCredentials,HTTPBearer
from users.models import *
from core.database import get_db
from sqlalchemy.orm import Session
import jwt
import datetime
security=HTTPBearer()
from core.config import setting


def get_authenticated_user(credentials:HTTPBasicCredentials=Depends(security),
                         db:Session=Depends(get_db)):
    return None



def generate_access_token(user_id:int,expire_in:int = 3600 ) ->str:
    now = datetime.datetime.utcnow()
    payload = {
        'user_id':user_id,
        'iat':now,
        'exp':now+datetime.timedelta(seconds=expire_in),
        'type':'access'
    }
        
    return jwt.encode(payload,setting.SECRET_KEY,algorithm='HS256')

def generate_refresh_token(user_id:int,expire_in:int = 3600* 24) ->str:
    now = datetime.datetime.utcnow()
    payload = {
        'user_id':user_id,
        'iat':now,
        'exp':now+datetime.timedelta(seconds=expire_in),
        'type':'refresh'
    }
        
    return jwt.encode(payload,setting.SECRET_KEY,algorithm='HS256')