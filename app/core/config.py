from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    Central configuration for the CDI API.
    Values are loaded from the .env file automatically.
    """

    # Application
    app_name: str = "Clinical Document Intelligence API"
    app_version: str = "0.1.0"
    debug: bool = False

    # Database
    mongodb_url: str = Field(default="mongodb://localhost:27017")
    mongodb_db_name: str = Field(default="cdi_db")

    # OpenAI
    openai_api_key: str = Field(default="")

    # Security
    api_key: str = Field(default="dev-api-key-change-in-production")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# This creates a single shared instance of Settings.
# Every other file imports this object — not the class itself.
# This is called the Singleton pattern.
settings = Settings()