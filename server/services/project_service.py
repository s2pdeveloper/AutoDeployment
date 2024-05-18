from config.mongo import mongo_client
from models.schemas import Project
from models.dto import ProjectRequest
db = mongo_client.get_database()
from fastapi import HTTPException
from utils.success import success, result
collection = db["project"]

class ProjectService:
    
    def __init__(self):
        pass
    
    async def create(self,data:ProjectRequest):
        project = collection.find_one({"name": data.name})
        if project:
            raise HTTPException(status_code=400, detail="Project Already Present With The Same Name")
        projectData = Project(**project)      
        collection.insert_one(projectData.dict())
        return success("Project Created successfully!")
    
    async def getAll(self,page:int,pageNumber:int):
        projects = collection.find({})
        count = collection.count({})
        return result({'count':count,'projects':projects})
        
        
        