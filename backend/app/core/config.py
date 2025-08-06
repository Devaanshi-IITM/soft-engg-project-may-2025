from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    SQLITE_URL: str = "sqlite:///../saathi_app.db"
    
    POSTGRES_USER: str = "myuser"
    POSTGRES_PASSWORD: str = "mypassword"
    POSTGRES_DB: str = "fastapi_db"
    POSTGRES_HOST: str = "postgres"  # <-- service name from docker-compose
    POSTGRES_PORT: str = "5432"
    POSTGRES_URL: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # MongoDB
    MONGO_HOST: str = "mongo"  # <-- service name
    MONGO_PORT: int = 27017
    MONGO_URL: str = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

    # Redis
    REDIS_HOST: str = "redis"  # <-- service name
    REDIS_PORT: int = 6379
    REDIS_URL: str = f"redis://{REDIS_HOST}:{REDIS_PORT}"

settings = Settings()
    