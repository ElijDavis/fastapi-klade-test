from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "production"
    PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
