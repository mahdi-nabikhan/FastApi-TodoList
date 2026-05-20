from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from core.config import setting
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session

engine = create_engine(
    setting.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

session = SessionLocal()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(engine)
