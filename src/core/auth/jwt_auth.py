from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from users.models import UserModel
from core.database import get_db
from sqlalchemy.orm import Session
import jwt
import datetime
from core.config import setting
from jwt.exceptions import DecodeError, InvalidSignatureError

security = HTTPBearer(auto_error=False)


def get_authenticated_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
      
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="توکن ارائه نشده یا فرمت Authorization اشتباه است (باید Bearer <token>)"
        )
    
    token = credentials.credentials
    
    try:
        decoded = jwt.decode(token, setting.SECRET_KEY, algorithms=["HS256"])
        
        
        if decoded.get("type") != "access":
            raise HTTPException(status_code=401, detail="Invalid token type: expected 'access'")
        
        user_id = decoded.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="user_id not found in token payload ")   
        
        user_obj = db.query(UserModel).filter_by(id=user_id).first()
        if not user_obj:
            raise HTTPException(status_code=401, detail="User not found")
        
        return user_obj
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidSignatureError:
        raise HTTPException(status_code=401, detail=" Invalid token signature ")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Malformed token (decoding error)  ")
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected auth error: {e}")
        raise HTTPException(status_code=401, detail="  Authentication failed due to internal error")

def decode_refresh_token(token: str):
    try:
        decoded = jwt.decode(token, setting.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded.get("user_id")  # درست: 'user_id' نه 'user_is'
        if not user_id:
            raise HTTPException(status_code=401, detail="user_id missing")
        if decoded.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")
        exp_timestamp = decoded.get("exp")
        if datetime.datetime.now().timestamp() > exp_timestamp:
            raise HTTPException(status_code=401, detail="Token expired")
        return user_id
    except InvalidSignatureError:
        raise HTTPException(status_code=401, detail="Invalid signature")
    except DecodeError:
        raise HTTPException(status_code=401, detail="Decode failed")
    except Exception as err:
        raise HTTPException(status_code=401, detail=f"Error: {str(err)}")


def generate_access_token(user_id:int,expire_in:int=3600)->str:
    now=datetime.datetime.now()
    payload = {
        'user_id':user_id,
         'iat': int(now.timestamp()), 
        'exp': int((now + datetime.timedelta(seconds=expire_in)).timestamp()),
        'type':'access'
    }
    
    return jwt.encode(payload,setting.SECRET_KEY,algorithm='HS256')

def generate_refresh_token(user_id:int,expire_in:int=3600*24)->str:
    now=datetime.datetime.now()
    payload = {
        'user_id':user_id,
        'iat': int(now.timestamp()), 
        'exp': int((now + datetime.timedelta(seconds=expire_in)).timestamp()),
        'type':'refresh'
    }
    
    return jwt.encode(payload,setting.SECRET_KEY,algorithm='HS256')