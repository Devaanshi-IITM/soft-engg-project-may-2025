# app/db/mongo.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = None
db = None

async def init_db():
    global client, db
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client.get_database("messages_db")

async def close_db():
    client.close()
