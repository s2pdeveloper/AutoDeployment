from pydoc import pager
from fastapi import APIRouter
from models.dto import ProjectRequest
from services.project_service import ProjectService

router = APIRouter()
projectService = ProjectService()

@router.post("")
async def create(data:ProjectRequest):
    return await projectService.create(data)

@router.get("")
async def getAll(page:int,pageNumber:int):
    return await projectService.getAll(page,pageNumber)