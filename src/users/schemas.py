from pydantic import BaseModel, Field, field_validator
from typing import Optional

from datetime import datetime


class UserLoginSchemas(BaseModel):
    username: str = Field(
        ..., max_length=150, min_length=5, description="username of The user"
    )
    password: str = Field(
        ..., max_length=150, min_length=5, description="password  of The user"
    )


class UserRegisterSchemas(BaseModel):
    username: str = Field(
        ..., max_length=150, min_length=5, description="username of The user"
    )
    password: str = Field(
        ..., max_length=150, min_length=5, description="password  of The user"
    )
    password_confirm: str = Field(
        ..., max_length=150, min_length=5, description="password  of The user"
    )

    @field_validator("password_confirm")
    def check_password(cls, password_confirm, validation):
        if not (password_confirm == validation.data.get("password")):
            raise ValueError("password not match")
        return password_confirm


class UserRefreshSchemas(BaseModel):
    token: str = Field(..., description="refresh token object")
