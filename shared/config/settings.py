
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "NexusAI"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    HOST: str = "127.0.0.1"

    PORT: int = 8000

    NEWS_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()  # settings = Settings() instead of Settings() Because now anywhere we can simply from shared.config.settings import settings print(settings.APP_NAME) Only one object exists. This is called a Singleton Configuration Pattern.