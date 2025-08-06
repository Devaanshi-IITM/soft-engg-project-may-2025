from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.db_conn import postgres, sqlite, mongo, redis # Import database initialization functions
from app.api.router import api_router  # Import the API router from the api module


app = FastAPI()
# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.on_event("startup")
async def startup():
    # sqlite.init_db()
    postgres.init_db()
    await mongo.init_db()
    await redis.init_redis()

@app.on_event("shutdown")
async def shutdown():
    # pass
    await mongo.close_db()
    await redis.close_redis()

app.include_router(
    api_router,  # Import the API router
    prefix=settings.API_V1_STR,  # Use the API version prefix from settings
    tags=["v1"],  # Tag for versioning
)