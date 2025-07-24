from fastapi import APIRouter

from app.api.routes import user, reminder, message, content, auth, ai

api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(auth.router)
api_router.include_router(reminder.router)
api_router.include_router(message.router)
api_router.include_router(content.router)
api_router.include_router(ai.router)

