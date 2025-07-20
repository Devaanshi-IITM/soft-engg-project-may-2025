# app/db/redis.py
import aioredis
from app.core.config import settings

redis = None

async def init_redis():
    global redis
    redis = await aioredis.from_url(settings.REDIS_URL, decode_responses=True)

async def close_redis():
    await redis.close()
