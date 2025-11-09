from aiogram import Dispatcher, Bot
import config
import asyncio
from database import create_tables
from handlers import start_router, film_router, save_video_router
from flask import Flask

dispatcher = Dispatcher()
bot = Bot(token=config.BOT_TOKEN)
app = Flask(__name__)

async def main():
    dispatcher.include_router(start_router)
    dispatcher.include_router(film_router)
    dispatcher.include_router(save_video_router)
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    create_tables()
    asyncio.run(main())
    app.run(host='0.0.0.0', debug=True, port=5000)