import redis.asyncio as redis
from app.core.config import settings
import json

r = redis.Redis(host=settings.REDIS_HOST, port=6379, decode_responses=True)

async def get_cached_location(key: str):
    value = await r.get(f"geo:{key}")
    return json.loads(value) if value else None

async def set_cached_location(key: str, value: dict):
    await r.set(f"geo:{key}", json.dumps(value), ex=3600)