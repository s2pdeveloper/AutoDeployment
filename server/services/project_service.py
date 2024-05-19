from datetime import datetime
from config.mongo import mongo_client
from models.schemas import Project
db = mongo_client.get_database()
from fastapi import HTTPException
from utils.success import success, result
from utils.projects import projects
collection = db["project"]

class ProjectService:
    
    def __init__(self,helperService):
        self.helperService = helperService
    
    async def create(self):
        try:
            if len(projects) == 0:
                raise HTTPException(status_code=400, detail="No Project Found")
            for project in projects:
                project['createdAt'] = datetime.now()   
                project['updatedAt'] = datetime.now()  
                projectData = Project(**project)   
                if projectData.userName:
                        projectData.userName = await self.helperService.encrypt(projectData.userName)
                
                if projectData.password:
                        projectData.password = await self.helperService.encrypt(projectData.password)
                
                collection.update_one(
                {"name": projectData.name},  # Filter criteria
                {"$setOnInsert": projectData.dict()},  # Update document with $setOnInsert
                upsert=True
                )
                
            return success("Projects Created successfully!")
        
        except Exception as e:
                print(str(e))
                raise HTTPException(status_code=500, detail=str(e))
    
    async def getAll(self,page:str,pageSize:str):
        try:
            count = collection.count_documents({})
            skip = max(0, int(page) - 1) * int(pageSize)
            projects = collection.find({},{"userName":0,"password":0,"createdAt":0,"updatedAt":0}).sort("createdAt", -1).skip(int(skip)).limit(int(pageSize))
            projects_list = []
            for document in projects:
            # Convert ObjectId to string
                print(document)
                if "_id" in document:
                    document["_id"] = str(document["_id"])
                    projects_list.append(document)
            return result({'count':count,'projects':projects_list})
        except Exception as e:
                    print(str(e))
                    raise HTTPException(status_code=500, detail=str(e))
        
        
        