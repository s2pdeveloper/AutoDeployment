import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig,MessageType
from dotenv import load_dotenv
from pathlib import Path
from fastapi import HTTPException
from utils.success import success

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_FROM=os.getenv('MAIL_FROM'),
    MAIL_PORT=os.getenv('MAIL_PORT'),
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME=os.getenv('MAIL_FROM_NAME'),
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)
class Mailer:
    def __init__(self):
        pass
    
    async def sendEmail(self,subject: str, email_to: str, body: dict):
        try:
        
            message = MessageSchema(
                subject=subject,
                recipients=[email_to],
                body=body,
                subtype= MessageType.plain
            )
            print("conf----",conf)
            fm = FastMail(conf)
            await fm.send_message(message)
            return success("Message Sent")
        
        except Exception as e:
                print(str(e))
                raise HTTPException(status_code=500, detail=str(e))
    

