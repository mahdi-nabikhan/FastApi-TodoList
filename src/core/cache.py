from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from core.config import setting
@asynccontextmanager
async def lifespan(app: FastAPI):
  
    redis_client = aioredis.from_url(
        setting.REDIS_URL,  
        encoding="utf8",
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    yield

    await redis_client.close()

app = FastAPI(lifespan=lifespan)

