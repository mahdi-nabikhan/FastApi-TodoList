from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import jwt

from users.models import UserModel
from core.database import get_db
from core.config import setting




def get_authenticated_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    # 1. No token provided
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing (Bearer token required)",
        )

    token = credentials.credentials

    try:
        # 2. Decode token
        payload = jwt.decode(
            token,
            setting.SECRET_KEY,
            algorithms=["HS256"]
        )

        # 3. Token type check
        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type (access token required)",
            )

        # 4. Extract user_id
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload (user_id missing)",
            )

        # 5. Find user
        user = db.query(UserModel).filter_by(id=user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )

        return user

    # 6. Token expired
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )

    # 7. Invalid signature
    except jwt.InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token signature",
        )

    # 8. Malformed token
    except jwt.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Malformed token",
        )

    # 9. Catch unexpected errors
    except Exception as e:
        print(f"Auth unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Authentication service error",
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