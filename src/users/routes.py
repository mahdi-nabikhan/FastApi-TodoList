from fastapi import APIRouter, Path, Depends, HTTPException, Query, status
from users.models import *
from fastapi.responses import JSONResponse
from users.schemas import *
from sqlalchemy.orm import Session
from users.utils import generate_token
from core.database import get_db
from typing import List
from core.auth.jwt_auth import *
from core.email_util import send_email
router = APIRouter(tags=["users router"])


@router.post("/login")
async def user_login(request: UserLoginSchemas, db: Session = Depends(get_db)):
    user_obj = db.query(UserModel).filter_by(username=request.username).first()
    if not user_obj:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="username doesnt exist"
        )
    if not user_obj.varify_passwod(request.password):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="inavlid password"
        )
    token_obj = TokenModel(user_id=user_obj.id, token=generate_token())
    db.add(token_obj)
    db.commit()
    db.refresh(token_obj)
    return JSONResponse(
        content={"detail": "user logged in successfully", "token": token_obj.token}
    )


@router.post("/register")
async def user_register(request: UserRegisterSchemas, db: Session = Depends(get_db)):
    if db.query(UserModel).filter_by(username=request.username).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="username already exist"
        )
    user_obj = UserModel(username=request.username)
    user_obj.set_password(request.password)
    db.add(user_obj)
    db.commit()

    return JSONResponse(content="user registerd successfully")


@router.post("/login/jwt")
async def user_login_jwt(request: UserLoginSchemas, db: Session = Depends(get_db)):
    user_obj = db.query(UserModel).filter_by(username=request.username).first()
    if not user_obj:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="username doesnt exist"
        )
    if not user_obj.varify_passwod(request.password):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="inavlid password"
        )
    access_token = generate_access_token(user_id=user_obj.id)
    refresh_token = generate_refresh_token(user_id=user_obj.id)
    response =  JSONResponse(
        content={
            "detail": "user logged in successfully",
            "access token": access_token,
            "refresh token": refresh_token,
        }
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 15,
    )
    response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite='lax',
        max_age=60 * 60 * 24 * 7
    )
    return response

@router.post("/refresh_token")
async def user_refresh_token(
    request: UserRefreshSchemas, db: Session = Depends(get_db)
):
    user_id = decode_refresh_token(request.token)
    access_token = generate_access_token(user_id=user_id)
    return JSONResponse(
        content={"detail": "user logged in successfully", "refresh token": access_token}
    )

@router.post("/send-test-email")
async def test_email():
    await send_email(
        subject="Test Email",
        recipients=["user@example.com"],
        body="<h1>Hello</h1><p>This is a test email.</p>"
    )
    return {"message": "Email sent"}