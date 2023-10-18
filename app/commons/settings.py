from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    users_ms: str
    authentication_ms: str


settings = Settings()
