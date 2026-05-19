from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as task_router
from fastapi_swagger import patch_fastapi
from users.routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware
@asynccontextmanager
async def lifespan(app:FastAPI):
    yield
    
    
 
app =FastAPI(lifespan=lifespan,docs_url=None,swagger_ui_oauth2_redirect_url=None)
patch_fastapi(app=app,docs_url='/swagger')
app.include_router(task_router)
app.include_router(user_router)


origins = [
    'http://127.0.0.1:3000',
    'http://localhost:3000']

app.middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_mehods = [''],
    allow_headers = [''] 
)