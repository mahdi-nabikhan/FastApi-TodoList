# tests/test_users/test_users_route.py
import pytest
from fastapi import status
from users.models import UserModel, TokenModel
from core.database import get_db
from main import app
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from core.auth.jwt_auth import generate_access_token, generate_refresh_token, decode_refresh_token

# فرض: client و db_session در conftest.py به صورت fixture تعریف شده‌اند

class TestUserRegister:
    def test_register_new_user_success(self, client: TestClient, db_session: Session):
        response = client.post("/register", json={
            "username": "newuser",
            "password": "secret123",
            "password_confirm": "secret123"
        })
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == "user registerd successfully"
        user = db_session.query(UserModel).filter_by(username="newuser").first()
        assert user is not None
        assert user.varify_passwod("secret123") is True

    def test_register_existing_user_fails(self, client: TestClient, db_session: Session):
        user = UserModel(username="existing")
        user.set_password("pass123")
        db_session.add(user)
        db_session.commit()

        response = client.post("/register", json={
            "username": "existing",
            "password": "newpass123",
            "password_confirm": "newpass123"
        })
        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json()["detail"] == "username already exist"

    def test_register_password_mismatch_fails(self, client: TestClient):
        response = client.post("/register", json={
            "username": "mismatch",
            "password": "pass123",
            "password_confirm": "pass456"
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestUserLogin:
    def test_login_success_returns_token(self, client: TestClient, db_session: Session):
        user = UserModel(username="loginuser")
        user.set_password("correctpass")
        db_session.add(user)
        db_session.commit()

        response = client.post("/login", json={
            "username": "loginuser",
            "password": "correctpass"
        })
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["detail"] == "user logged in successfully"
        assert "token" in data
        token_record = db_session.query(TokenModel).filter_by(token=data["token"]).first()
        assert token_record is not None
        assert token_record.user_id == user.id

    def test_login_wrong_username_fails(self, client: TestClient):
        response = client.post("/login", json={
            "username": "nonexistent",
            "password": "anypass123"
        })
        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json()["detail"] == "username doesnt exist"

    def test_login_wrong_password_fails(self, client: TestClient, db_session: Session):
        user = UserModel(username="wrongpass")
        user.set_password("correctpass")
        db_session.add(user)
        db_session.commit()

        response = client.post("/login", json={
            "username": "wrongpass",
            "password": "wrongpass123"
        })
        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json()["detail"] == "inavlid password"


class TestUserLoginJWT:
    def test_login_jwt_success(self, client: TestClient, db_session: Session):
        user = UserModel(username="jwtuser")
        user.set_password("jwtpass")
        db_session.add(user)
        db_session.commit()

        response = client.post("/login/jwt", json={
            "username": "jwtuser",
            "password": "jwtpass"
        })
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["detail"] == "user logged in successfully"
        assert "access token" in data
        assert "refresh token" in data

    def test_login_jwt_invalid_credentials(self, client: TestClient):
        response = client.post("/login/jwt", json={
            "username": "invalid",
            "password": "invalidpass"
        })
        assert response.status_code == status.HTTP_409_CONFLICT


class TestRefreshToken:
    def test_refresh_token_success(self, client: TestClient, db_session: Session):
        # ابتدا لاگین کرده و refresh token بگیریم
        user = UserModel(username="refuser")
        user.set_password("refpass")
        db_session.add(user)
        db_session.commit()

        login_resp = client.post("/login/jwt", json={
            "username": "refuser",
            "password": "refpass"
        })
        refresh_token = login_resp.json()["refresh token"]

        response = client.post("/refresh_token", json={"token": refresh_token})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["detail"] == "user logged in successfully"
        assert "refresh token" in data

    def test_refresh_token_invalid_fails(self, client: TestClient):
        response = client.post("/refresh_token", json={"token": "invalid.token.string"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED  # یا 400 بسته به پیاده‌سازی