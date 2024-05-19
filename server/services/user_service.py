import os
from config.mongo import mongo_client
from models.dto import ChangePassword, Login
from models.schemas import User
db = mongo_client.get_database()
from fastapi import HTTPException
from utils.success import success
collection = db["user"]

class UserService:
    def __init__(self,mailerService,helperService):
        self.mailerService = mailerService
        self.helperService = helperService
        
    async def login(self,data:Login):
        userData = collection.find_one({"email": data.email})
        if userData:
            user = User(**userData)
            if user.otp and data.otp:
                rawOTP = await self.helperService.decrypt(user.otp)
                if rawOTP == data.otp:
                    collection.update_one({"email": data.email},{ "$unset": { "otp": 1 } })
                    return success("Login successfully!")
                else:
                    raise HTTPException(status_code=400, detail="Incorrect password")
          
        else:
            raise HTTPException(status_code=400, detail="User not found!")
        
    
    # async def changePassword(self,id:str,data:ChangePassword):
    #     userData = collection.find_one({"_id": id})
    #     if userData:
    #         user = User(**userData)
    #         user.set_password(data.newPassword)
    #         collection.insert_one(user.dict())
    #         return success("Password Changed successfully!")
    #     else:
    #         raise HTTPException(status_code=400, detail="User not found!")
            
                
    async def otpGenerate(self,email:str):  
        try:
            userData = collection.find_one({"email": email})
            if userData:
                otp = await self.helperService.generateOTP()
                encodedOtp = await self.helperService.encrypt(str(otp))
                message = f"OTP is {otp}"
                subject="OTP"
                res = await self.mailerService.sendEmail(subject,os.getenv('MAIL_USERNAME'),message)
                collection.update_one({"email": email},{ "$set": { "otp": encodedOtp } })
                return success("OTP has been sent to Email successfully!")
                
            else:
                raise HTTPException(status_code=400, detail="User not found!")
            
        except Exception as e:
                print(str(e))
                raise HTTPException(status_code=500, detail=str(e))
        