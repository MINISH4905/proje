from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI App"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
