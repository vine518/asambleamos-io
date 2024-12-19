import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    jwt_secret_key: str
    mistral_api_key: str
    algorithm: str
    access_token_expire_minutes: int
    debug: bool = False

    class Config:
        env_file = ".env.local"


def get_property(name):
    return getattr(settings, name, None)


settings = Settings()
