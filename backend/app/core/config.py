from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    PROJECT_NAME: str = "Pharmora AI"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "pharmora-secret-change"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    DATABASE_URL: str = "postgresql://pharmora:pharmora@localhost:5432/pharmora"
    REDIS_URL: str = "redis://localhost:6379/0"
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "pharmora123"
    QDRANT_URL: str = "http://localhost:6333"
    class Config:
        env_file = ".env"
settings = Settings()
