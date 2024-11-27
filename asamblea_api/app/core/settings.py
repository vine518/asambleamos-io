import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    jwt_secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    debug: bool = False

    class Config:
        env_file = ".env"


def get_property(name):
    return os.getenv(name)


settings = Settings()
