from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from config import setting
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.orm import Session





engine = create_engine (
    setting.SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread':False}
)
SessionLocal = sessionmaker(autocommit =False,autoflush=False,bind=engine)
Base = declarative_base()

session = SessionLocal()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__= 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    firstname = Column(String(length=30))
    lastname = Column(String(50))
    age = Column(Integer)
    code = Column(Integer)
    
    
    def __repre__(self):
        return f'User(id ={self.id},firstname={self.firstname})'
    

    
    
    
    
    
    

    
Base.metadata.create_all(engine)