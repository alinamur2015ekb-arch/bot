from aiogram import Bot, Dispatcher
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    token: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()

API_TOKEN = settings.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
