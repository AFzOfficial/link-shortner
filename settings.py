import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Link Shortner"
    DEBUG: bool = True
    SECRET_KEY: str = 'secret'
    API_PREFIX: str = "api"
    API_VERSION: str = "v1"
    ALLOWED_ORIGINS: list = ["*"]

    DATETIME_TIMEZONE: str = 'Asia/Tehran'
    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    TOKEN_EXPIRE_SECONDS : int = 86400 # Expiration time, unit: seconds ( 86400 = 1 * 24 * 60 * 60)
    TOKEN_SECRET_KEY : str = 'jwt_secret'
    TOKEN_ALGORITHM : str = 'HS256'

    class Config:
        env_file = ".env"

settings = Settings()
