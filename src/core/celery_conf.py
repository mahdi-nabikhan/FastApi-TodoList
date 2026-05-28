
from celery import Celery
from core.config import setting

celery_app = Celery(
    "worker",
    broker=setting.CELERY_BROKER_URL,
    backend=setting.CELERY_BACKEND_URL,
)

# Optional Celery Config
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@celery_app.task
def hello_world():
    return "Hello World"

