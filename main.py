import asyncio
from config import bot, dp
from hendlers import router
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import uvicorn
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не установлен в переменных окружения!")
WEBHOOK_URL_BASE = os.getenv("WEBHOOK_URL_BASE")
if not WEBHOOK_URL_BASE:
    raise ValueError("WEBHOOK_URL_BASE не установлен в переменных окружения!")
WEBHOOK_PATH = "/webhook" 
WEBHOOK_URL = f"{WEBHOOK_URL_BASE}{WEBHOOK_PATH}" 
WEBHOOK_SECRET_TOKEN = os.getenv("WEBHOOK_SECRET_TOKEN", "your_super_secret_token_here")
if WEBHOOK_SECRET_TOKEN == "your_super_secret_token_here":
    print("ВНИМАНИЕ: Используется дефолтный секретный токен для Webhook. Рекомендуется установить свой через переменную окружения WEBHOOK_SECRET_TOKEN.")
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Запуск приложения FastAPI...")
    if not isinstance(bot, Bot):
        pass
    
    if not isinstance(dp, Dispatcher):
        pass

    dp.include_router(router)

    print(f"Устанавливаем Webhook на URL: {WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL, secret_token=WEBHOOK_SECRET_TOKEN)
    print("Webhook установлен.")
    yield 
    print("Остановка приложения FastAPI...")
    print("Удаляем Webhook...")
    await bot.delete_webhook()
    print("Webhook удален.")
    await dp.stop_polling()
    await bot.session.close() 

app = FastAPI(lifespan=lifespan)

@app.post(WEBHOOK_PATH)
async def bot_webhook(request: Request):
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != WEBHOOK_SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid secret token")
    update_json = await request.json()
    update = types.Update.model_validate(update_json)
    await dp.feed_update(bot, update)
    return {"status": "ok"}
@app.get("/")
async def read_root():
    return {"message": "Бот запущен и ожидает Webhook!"}
if __name__ == "__main__":
    print("Запуск FastAPI локально. Для работы Webhook нужен публичный URL (например, ngrok).")
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
