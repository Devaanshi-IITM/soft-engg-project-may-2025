from app.core.db.postgres import SessionLocal
from app.core.db.mongo import db as mongo_db
from app.core.db.redis import redis_client as redis

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_mongo_db():
    try:
        yield mongo_db
    finally:
        # No explicit close needed for motor, but can be used if needed
        pass

def get_redis():
    try:
        yield redis
    finally:
        # No explicit close needed for aioredis, but can be used if needed
        pass