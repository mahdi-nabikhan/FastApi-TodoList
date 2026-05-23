import pytest
from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker, Session
from core.database import Base
from tasks.models import TaskModel
from users.models import pwd_context,UserModel,TokenModel




@pytest.fixture(scope="function")
def db_session():
    """ایجاد session با دیتابیس SQLite in-memory و فعال‌سازی Foreign Keys از طریق event"""
    engine = create_engine("sqlite:///:memory:", echo=False)

    @event.listens_for(engine, "connect")
    def enable_foreign_keys(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)


class TestUserModel:
    def test_create_user(self, db_session: Session):
        user = UserModel(username="testuser")
        user.set_password("mysecret")
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        assert user.id is not None
        assert user.username == "testuser"
        assert user.is_active is False
        assert user.password != "mysecret"
        assert user.varify_passwod("mysecret") is True
        assert user.varify_passwod("wrong") is False

    def test_hash_password_returns_different_hash(self, db_session: Session):
        user = UserModel(username="hashuser")
        hash1 = user.hash_password("samepass")
        hash2 = user.hash_password("samepass")
       
        assert hash1 != hash2
      
        assert pwd_context.verify("samepass", hash1) is True

    def test_set_password_sets_hashed_password(self, db_session: Session):
        user = UserModel(username="setpassuser")
        user.set_password("newpass123")
        assert user.password is not None
        assert user.varify_passwod("newpass123") is True

    def test_verify_password_fails_on_wrong(self, db_session: Session):
        user = UserModel(username="verifyuser")
        user.set_password("correct")
        assert user.varify_passwod("wrong") is False

    def test_username_nullable_false(self, db_session: Session):
        with pytest.raises(Exception):
            user = UserModel(username=None)
            db_session.add(user)
            db_session.commit()



class TestTaskModel:
    def test_create_task_with_user(self, db_session: Session):
        user = UserModel(username="taskowner")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        task = TaskModel(
            user_id=user.id,
            title="My Task",
            description="Do something",
            is_complated=False
        )
        db_session.add(task)
        db_session.commit()
        db_session.refresh(task)

        assert task.id is not None
        assert task.user_id == user.id
        assert task.title == "My Task"
        assert task.description == "Do something"
        assert task.is_complated is False
        assert task.created_date is not None
        assert task.updated_date is not None

    @pytest.mark.skip(reason="SQLite have no limit on VARCHAR  ")
    def test_task_title_max_length(self, db_session: Session):

        user = UserModel(username="maxlengthuser")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()

        long_title = "a" * 101
        task = TaskModel(user_id=user.id, title=long_title)
        with pytest.raises(Exception):
            db_session.add(task)
            db_session.commit()

    def test_task_is_complated_default_false(self, db_session: Session):
        user = UserModel(username="defaultuser")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()

        task = TaskModel(user_id=user.id, title="No completion flag")
        db_session.add(task)
        db_session.commit()
        db_session.refresh(task)
        assert task.is_complated is False

    def test_task_description_nullable_true(self, db_session: Session):
        user = UserModel(username="descnull")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()

        task = TaskModel(user_id=user.id, title="No desc", description=None)
        db_session.add(task)
        db_session.commit()
        db_session.refresh(task)
        assert task.description is None

    def test_task_relationship_back_populates(self, db_session: Session):
        user = UserModel(username="reluser")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()

        task1 = TaskModel(user_id=user.id, title="Task 1")
        task2 = TaskModel(user_id=user.id, title="Task 2")
        db_session.add_all([task1, task2])
        db_session.commit()

        db_session.refresh(user)
        assert len(user.tasks) == 2
        assert task1.user.username == "reluser"

class TestTokenModel:
    def test_create_token(self, db_session: Session):
        user = UserModel(username="tokenuser")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        token = TokenModel(user_id=user.id, token="abc123xyz")
        db_session.add(token)
        db_session.commit()
        db_session.refresh(token)

        assert token.id is not None
        assert token.token == "abc123xyz"
        assert token.created_data is not None

    def test_token_unique_constraint(self, db_session: Session):
        user = UserModel(username="uniqueuser")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()

        token1 = TokenModel(user_id=user.id, token="same_token")
        token2 = TokenModel(user_id=user.id, token="same_token")
        db_session.add(token1)
        db_session.commit()
        db_session.add(token2)
        with pytest.raises(Exception):  # UniqueViolation
            db_session.commit()

    def test_token_user_relationship(self, db_session: Session):
        user = UserModel(username="reltoken")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        token = TokenModel(user_id=user.id, token="rel_token_value")
        db_session.add(token)
        db_session.commit()
        db_session.refresh(token)

        assert token.user.username == "reltoken"

    def test_token_created_data_auto_set(self, db_session: Session):
        user = UserModel(username="dateuser")
        user.set_password("pass")
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        token = TokenModel(user_id=user.id, token="date_token")
        db_session.add(token)
        db_session.commit()
        db_session.refresh(token)
        assert token.created_data is not None



def test_task_foreign_key_constraint(db_session: Session):
    task = TaskModel(user_id=9999, title="Invalid user")
    db_session.add(task)
    with pytest.raises(Exception):  # IntegrityError
        db_session.commit()


def test_token_foreign_key_constraint(db_session: Session):
    token = TokenModel(user_id=9999, token="invalid_fk")
    db_session.add(token)
    with pytest.raises(Exception):
        db_session.commit()