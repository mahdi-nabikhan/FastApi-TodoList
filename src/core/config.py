from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    SECRET_KEY: str = "test"
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".env")
    REDIS_URL :str
    
    
    MAIL_USERNAME: str = ""          
    MAIL_PASSWORD: str = ""               
    MAIL_FROM: str   ='no-replay@example.com'               
    MAIL_PORT: int = 25
    MAIL_SERVER: str    ='smtp4dev' 
    MAIL_FROM_NAME :str = 'Admin'             
    MAIL_STARTTLS: bool = False        
    MAIL_SSL_TLS: bool = False        

    
    CELERY_BROKER_URL:str = 'redis://redis:6479/3'
    CELERY_BACKEND_URL:str ='redis://redis:6479/3'


setting = Settings()
