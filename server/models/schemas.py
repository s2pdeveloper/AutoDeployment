from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
# import bcrypt

class User(BaseModel):
    name: str
    email: EmailStr
    otp:Optional[str] = None
    address: Optional[str] = None
    
    # def set_password(self, password: str):
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
    #     self.password = hashed_password.decode('utf-8')

    # def verify_password(self, password: str) -> bool:
    #     return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class Action(str,Enum):
    PULL = "PULL"
    STOP = "STOP"
    START = "START"
    RESTART = "RESTART"
    STATUS = "STATUS"
    
class Status(str,Enum):
    RUNNING = "RUNNING"
    STOP = "STOP"
    TERMINATE = "TERMINATE"

        
class Project(BaseModel):
     name: str
     processName:str
     status: Status = Status.STOP
     userName: str
     password: str
     filePath: Optional[str] = None
     scriptPath:  Optional[str] = None
     createdAt: datetime
     updatedAt:datetime
    #  action: Action
    