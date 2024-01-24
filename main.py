import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.enums import ParseMode

import config

from app.handlers.basic import basic_router
from app.handlers.callback import callback_router
from app.handlers.pay import pay_router
from app.handlers.form import form_router
from app.handlers.send_media import media_router

from app.utils.commands import set_commands

from app.database.model import async_main


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(config.ADMIN_ID, text='Bot is running')


async def stop_bot(bot: Bot):
    await bot.send_message(config.ADMIN_ID, text='Bot stopped')


async def main():
    await async_main()
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_routers(basic_router, callback_router, pay_router, form_router, media_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Error')
    