from fastapi import APIRouter
from models.dto import ChangePassword, Login
from services.user_service import UserService

router = APIRouter()
userService = UserService()

@router.post("/login")
async def login(data:Login):
    return await userService.login(data)

@router.post("/changePassword/{id}")
async def changePassword(id:str,data:ChangePassword):
    return await userService.changePassword(id,data)

