from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPBasic,HTTPBasicCredentials,HTTPBearer,HTTPAuthorizationCredentials
from users.models import *
from core.database import get_db
from sqlalchemy.orm import Session
import jwt
import datetime
security=HTTPBearer()
from core.config import setting
from jwt.exceptions import DecodeError,ExpiredSignatureError,InvalidSignatureError
import datetime

def get_authenticated_user(credentials:HTTPAuthorizationCredentials=Depends(security),
                         db:Session=Depends(get_db)):
    
    token = credentials.credentials
    try:
        decoded = jwt.decode(token,setting.SECRET_KEY,algorithms='HS256')
        user_id = decoded.get('user_is',None)
        if not user_id :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Authenticatoin failed , User_id is not in payload')
        if not decoded.get('type') != 'access':
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Authenticatoin failed , token type is not valid')
        
        if not datetime.datetime.now() > datetime.datetime.timestamp(decoded.get('exp')) :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Authenticatoin failed , token expired')
        user_obj = db.query(UserModel).filter_by(id=user_id).one_or_none
        if user_obj == None :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Authenticatoin failed ,cant find aby user with this user id')
            
        return user_obj
        
    except InvalidSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Authenticatoin failed , invalid signture')
    except DecodeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Decode failed , invalid signture')
    except Exception as err:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Decode failed , invalid {err}')
    
   



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