from pydantic import BaseSettings

class Settings(BaseSettings):
    API_VI_STR: str = "/api/v1"
    POSTGRES_URL: str = "postgresql://user:password@localhost/fastapi_db"
    MONGO_URI: str = "mongodb://localhost:27017"
    REDIS_URL: str = "redis://localhost"

settings = Settings()
    