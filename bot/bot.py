from aiogram import Bot, Dispatcher

from misc import TgKey
from .handlers import router as all_router

async def start():
    bot = Bot(token=TgKey.TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(all_router)
    await dp.start_polling(bot, skip_updates=True)