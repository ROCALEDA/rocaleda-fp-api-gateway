from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    customers_ms: str
    users_ms: str
    authentication_ms: str
    candidates_ms: str
    orchestrator_ms: str


settings = Settings()
