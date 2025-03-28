# config.py
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///vehicles.db"
    MCP_HOST: str = "localhost"
    MCP_PORT: int = 9999

    class Config:
        env_file = ".env"

settings = Settings()
