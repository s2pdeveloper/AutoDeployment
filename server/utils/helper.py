import os
from config.mongo import mongo_client
from models.schemas import User
import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import math, random
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
db = mongo_client.get_database()
collection = db["user"]
key= os.getenv('SECRET_KEY')


class Helper:
    
    async def encrypt(self,raw:str): 
        raw = pad(raw.encode(),16)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        byteValue = base64.b64encode(cipher.encrypt(raw))
        return byteValue.decode('utf-8')
    
    async def decrypt(self,enc:str):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        byteValue = unpad(cipher.decrypt(enc),16)
        return byteValue.decode('utf-8')
    
    async def generateOTP(self):
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        OTP = ""
        length = len(string)
        for i in range(6) :
            OTP += string[math.floor(random.random() * length)]

        return OTP
    
    def adminInsertion(self):
        user = collection.find_one({"email": "superadmin@gmail.com"})
        if user is None:
            # Define your user data
            user_data = {
                "name": "Super admin",
                "email": "superadmin@gmail.com",
                "address": "s2p Edutech"
            }

            # Create a User object and hash the password
            user = User(**user_data)

            # Insert validated and hashed data into MongoDB
            result = collection.insert_one(user.dict())
            print(f"Inserted user with ID: {result.inserted_id}")
    