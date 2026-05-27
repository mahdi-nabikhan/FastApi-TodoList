from fastapi_mail import FastMail,MessageSchema,ConnectionConfig
from core.config import setting

conf=ConnectionConfig(
    MAIL_USERNAME=setting.MAIL_USERNAME,
    MAIL_PASSWORD=setting.MAIL_PASSWORD,
    MAIL_FROM=setting.MAIL_FROM,
    MAIL_PORT=setting.MAIL_PORT,
    MAIL_SERVER=setting.MAIL_SERVER,
    MAIL_FROM_NAME=setting.MAIL_FROM_NAME,
    MAIL_STARTTLS=setting.MAIL_STARTTLS,
    MAIL_SSL_TLS=setting.MAIL_SSL_TLS,
    MAIL_USE_CREDENTIALS=setting.MAIL_USE_CREDENTIALS,
    
)


async def send_email(subject: str, recipients: list, body: str):
    
    message = MessageSchema(
        subject=subject,
        recipients=recipients,
        body=body,
        subtype="html"  
    )
    fm = FastMail(config=conf)
    await fm.send_message(message)