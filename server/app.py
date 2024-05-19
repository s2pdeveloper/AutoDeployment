from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user,project
from utils.helper import Helper
app = FastAPI(swagger_ui_parameters={"displayRequestDuration": True})
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthCheck")
async def read_root():
    return {"message": "Server is Running"}

helper = Helper()
helper.adminInsertion()
app.include_router(user.router,
    prefix="/user",
    tags=["User"])

app.include_router(project.router,
    prefix="/project",
    tags=["Project"])

