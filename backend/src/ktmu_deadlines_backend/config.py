from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_ignore_empty=True)

    DATABASE_URL: AnyUrl


settings = Settings()  # pyright: ignore[reportCallIssue]
