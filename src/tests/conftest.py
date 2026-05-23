import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
SRC_DIR = ROOT_DIR / 'src'
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(SRC_DIR))

from fastapi.testclient import TestClient
from core.database import Base,create_engine,sessionmaker,get_db
from main import app
from sqlalchemy import StaticPool
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
from core.auth.jwt_auth import get_authenticated_user
SQLALCHEMY_DATABASE_URL ='sqlite:///:memory:'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def override_get_db():
    db = TestSessionLocal()

    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine)

client =TestClient(app)

@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()



@pytest.fixture(scope="session")
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
def test_user(db_session):
    from users.models import UserModel
    user = UserModel(username="testuser")
    user.set_password("secret")
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user



@pytest.fixture(scope="function")
def authenticated_client(client, test_user):
    def override_auth():
        return test_user
    app.dependency_overrides[get_authenticated_user] = override_auth
    yield client
    app.dependency_overrides.pop(get_authenticated_user, None)

@pytest.fixture(scope="function")
def db_session():
    
    connection = engine.connect()
    transaction = connection.begin()
    session = TestSessionLocal(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()