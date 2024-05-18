from config.mongo import mongo_client
from models.schemas import User
db = mongo_client.get_database()
collection = db["user"]

class Helper:
    
    def adminInsertion(self):
        user = collection.find_one({"email": "superadmin@gmail.com"})
        if user is None:
            # Define your user data
            user_data = {
                "name": "Super admin",
                "email": "superadmin@gmail.com",
                "password": "",
                "address": "s2p Edutech"
            }

            # Create a User object and hash the password
            user = User(**user_data)
            user.set_password("1234")

            # Insert validated and hashed data into MongoDB
            result = collection.insert_one(user.dict())
            print(f"Inserted user with ID: {result.inserted_id}")
    