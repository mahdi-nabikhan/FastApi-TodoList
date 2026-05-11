from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as task_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    yield
    
    
    
app =FastAPI(lifespan=lifespan)
app.include_router(task_router)