from celery import Celery
from core.config import setting

celery_app=Celery('worker',broker=setting.CELERY_BROKER_URL,backend=setting.CELERY_BACKEND_URL)



@celery_app.task
def hello_world():
    pass