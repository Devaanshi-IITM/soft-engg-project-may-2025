# app/db/mongo.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = None
db = None

async def init_db():
    global client, db
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client["message_db"]
    db.create_collection("messages")

async def close_db():
    client.close()
