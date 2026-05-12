from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

class Settings (BaseSettings):
    SQLALCHEMY_DATABASE_URL :str
    model_config = SettingsConfigDict(env_file=Path(__file__).parent/'.env')
    
    
    
setting=Settings()
