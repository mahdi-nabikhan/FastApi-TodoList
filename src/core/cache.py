from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.memory import InMemoryCacheBackend
from fastapi_cache.decorator import cache

app = FastAPI()
cache_backend = InMemoryCacheBackend()
FastAPICache.init(cache_backend)
