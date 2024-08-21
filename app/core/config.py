from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Library API"
    PROJECT_VERSION: str = "1.0.0"
    MONGO_URL: str = "mongodb://mongodb:27017"
    DATABASE_NAME: str = "library"

settings = Settings()
