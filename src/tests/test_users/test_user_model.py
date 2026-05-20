import pytest
from users.models import UserModel, TokenModel
from passlib.context import CryptContext
import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from core.auth.token_auth import get_authenticated_user
from users.models import UserModel, TokenModel
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class TestUserModel:
    def test_create_user(self, db_session):
        user = UserModel(username="testuser")
        user.set_password("mypassword")
        db_session.add(user)
        db_session.commit()

        assert user.id is not None
        assert user.username == "testuser"
        assert user.password is not None
        assert user.password != "mypassword"

    def test_verify_password(self, db_session):
        user = UserModel(username="testuser2")
        user.set_password("correct_password")
        db_session.add(user)
        db_session.commit()

        assert user.varify_passwod("correct_password") is True
        assert user.varify_passwod("wrong_password") is False




class TestGetAuthenticatedUser:
    def test_valid_token_returns_user(self, db_session: Session):
        # Arrange
        user = UserModel(username="testuser")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()
        token = TokenModel(user_id=user.id, token="valid_token")
        db_session.add(token)
        db_session.commit()

        credentials = HTTPAuthorizationCredentials(
            scheme="Bearer", credentials="valid_token"
        )

      
        result_user = get_authenticated_user(credentials, db_session)

       
        assert result_user.id == user.id
        assert result_user.username == user.username

    def test_invalid_token_raises_401(self, db_session: Session):
        credentials = HTTPAuthorizationCredentials(
            scheme="Bearer", credentials="invalid_token"
        )
        with pytest.raises(HTTPException) as exc:
            get_authenticated_user(credentials, db_session)
        assert exc.value.status_code == 401
        assert "invalid credentials" in exc.value.detail

    def test_token_not_in_db_raises_401(self, db_session: Session):
        credentials = HTTPAuthorizationCredentials(
            scheme="Bearer", credentials="nonexistent"
        )
        with pytest.raises(HTTPException) as exc:
            get_authenticated_user(credentials, db_session)
        assert exc.value.status_code == 401