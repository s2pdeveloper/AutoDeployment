from fastapi import APIRouter
from models.dto import ChangePassword, Login
from utils.helper import Helper
from utils.mailer import Mailer
from services.user_service import UserService

router = APIRouter()
mailerService = Mailer()
helperService = Helper()
userService = UserService(mailerService,helperService)

@router.post("/login")
async def login(data:Login):
    return await userService.login(data)

@router.get("/otp")
async def login(email:str):
    return await userService.otpGenerate(email)

# @router.post("/changePassword/{id}")
# async def changePassword(id:str,data:ChangePassword):
#     return await userService.changePassword(id,data)

