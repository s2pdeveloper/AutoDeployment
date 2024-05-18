from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from fastapi import status
from fastapi.responses import JSONResponse



class Login(BaseModel):
    email: EmailStr
    password: str
    
class ChangePassword(BaseModel):
    newPassword: str
    oldPassword: str
    
class ProjectRequest(BaseModel):
     name: str
     userName: Optional[str] = None
     password: Optional[str] = None
     filePath: Optional[str] = None
     status:Optional[str] = None