from config.mongo import mongo_client
from models.dto import ChangePassword, Login
from models.schemas import User
db = mongo_client.get_database()
from fastapi import HTTPException
from utils.success import success
collection = db["user"]
class UserService:
    def __init__(self):
        pass
    async def login(self,data:Login):
        print("inside user service-----")
        userData = collection.find_one({"email": data.email})
        print("user_data----",userData)
        if userData:
            user = User(**userData)
            print("user----",user)
            
            if user.verify_password(data.password):
                return success("Login successfully!")
            else:
                raise HTTPException(status_code=400, detail="Incorrect password")
                
        else:
            
            raise HTTPException(status_code=400, detail="User not found!")
        
    
    async def changePassword(self,id:str,data:ChangePassword):
        userData = collection.find_one({"_id": id})
        if userData:
            user = User(**userData)
            user.set_password(data.newPassword)
            collection.insert_one(user.dict())
            return success("Password Changed successfully!")
        else:
            raise HTTPException(status_code=400, detail="User not found!")
            
                
        
        