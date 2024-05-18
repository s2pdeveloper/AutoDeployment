from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
import bcrypt

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: Optional[str] = None
    
    def set_password(self, password: str):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
        self.password = hashed_password.decode('utf-8')

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class Action(str,Enum):
    PULL = "PULL"
    STOP = "STOP"
    START = "START"
    RESTART = "RESTART"
    STATUS = "STATUS"
        
class Project(BaseModel):
     name: str
     status: str
     userName: str
     password: str
     filePath: str
    #  action: Action
    