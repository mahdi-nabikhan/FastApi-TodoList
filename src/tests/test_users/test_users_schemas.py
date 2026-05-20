import pytest
from pydantic import ValidationError
from users.schemas import (
    UserLoginSchemas,
    UserRegisterSchemas,
    UserRefreshSchemas,
)


class TestUserLoginSchemas:
    def test_valid_login(self):
        data = {"username": "validuser", "password": "pass123"}
        schema = UserLoginSchemas(**data)
        assert schema.username == "validuser"
        assert schema.password == "pass123"

    def test_username_too_short(self):
        data = {"username": "a", "password": "pass123"}
        with pytest.raises(ValidationError) as exc:
            UserLoginSchemas(**data)
        errors = exc.value.errors()
        # بررسی وجود خطای طول کم برای فیلد username
        assert any(
            err["type"] == "string_too_short" and err["loc"][0] == "username"
            for err in errors
        )

    def test_username_too_long(self):
        data = {"username": "a" * 151, "password": "pass123"}
        with pytest.raises(ValidationError) as exc:
            UserLoginSchemas(**data)
        errors = exc.value.errors()
        assert any(
            err["type"] == "string_too_long" and err["loc"][0] == "username"
            for err in errors
        )

    def test_password_too_short(self):
        data = {"username": "validuser", "password": "123"}
        with pytest.raises(ValidationError):
            UserLoginSchemas(**data)


class TestUserRegisterSchemas:
    def test_valid_registration(self):
        data = {
            "username": "newuser",
            "password": "secret123",
            "password_confirm": "secret123",
        }
        schema = UserRegisterSchemas(**data)
        assert schema.username == "newuser"
        assert schema.password == "secret123"
        assert schema.password_confirm == "secret123"

    def test_password_mismatch(self):
        data = {
            "username": "newuser",
            "password": "secret123",
            "password_confirm": "wrongpass",
        }
        with pytest.raises(ValidationError) as exc:
            UserRegisterSchemas(**data)
        errors = exc.value.errors()
        
        assert any("password not match" in err["msg"] for err in errors)

    def test_missing_password_confirm(self):
        data = {"username": "newuser", "password": "secret123"}
        with pytest.raises(ValidationError):
            UserRegisterSchemas(**data)

    def test_username_too_long(self):
        data = {
            "username": "a" * 151,
            "password": "secret123",
            "password_confirm": "secret123",
        }
        with pytest.raises(ValidationError):
            UserRegisterSchemas(**data)


class TestUserRefreshSchemas:
    def test_valid_token(self):
        data = {"token": "some.refresh.token"}
        schema = UserRefreshSchemas(**data)
        assert schema.token == "some.refresh.token"

    def test_missing_token(self):
        with pytest.raises(ValidationError):
            UserRefreshSchemas(**{})