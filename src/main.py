from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as task_router
from fastapi_swagger import patch_fastapi


@asynccontextmanager
async def lifespan(app:FastAPI):
    yield
    
    
    
app =FastAPI(lifespan=lifespan,docs_url=None,swagger_ui_oauth2_redirect_url=None)
patch_fastapi(app=app,docs_url='/swagger')
app.include_router(task_router)