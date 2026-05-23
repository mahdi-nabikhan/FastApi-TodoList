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
    if not credentials or credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Authentications failled token not provided'
        )
    token = credentials.credentials
    try:
        decoded = jwt.decode(token, setting.SECRET_KEY, algorithms=["HS256"])

        user_id = decoded.get("user_id")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication failed: user_id not in payload",
            )

        if decoded.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication failed: token type is not access",
            )

        # اصلاح بررسی انقضا
        exp_timestamp = decoded.get("exp")
        if not exp_timestamp:
            raise HTTPException(status_code=401, detail="No expiration in token")
        current_timestamp = datetime.datetime.now().timestamp()
        if current_timestamp > exp_timestamp:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication failed: token expired",
            )

        user_obj = db.query(UserModel).filter_by(id=user_id).one_or_none()
        if user_obj is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication failed: user not found",
            )

        return user_obj

    except InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed: invalid signature",
        )
    except DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed: decode error",
        )
    except HTTPException:
        raise
    except Exception as err:
        #
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication failed: {str(err)}",
        )


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