from fastapi import APIRouter
from models.dto import ProjectRequest
from utils.helper import Helper
from services.project_service import ProjectService

router = APIRouter()
helperService = Helper()
projectService = ProjectService(helperService)

@router.post("")
async def create():
    return await projectService.create()

@router.get("")
async def getAll(page:str,pageNumber:str):
    return await projectService.getAll(page,pageNumber)