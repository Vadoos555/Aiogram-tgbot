from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='START'),
        BotCommand(command='help', description='HELP'),
        BotCommand(command='reply', description='Show reply buttons'),
        BotCommand(command='inline', description='Show inline buttons'),
        BotCommand(command='pay', description='Buy a product'),
        BotCommand(command='form', description='Fill the form'),
        BotCommand(command='audio', description='Sending audio'),
        BotCommand(command='document', description='Sending document'),
        BotCommand(command='mediagroup', description='Sending mediagroup'),
        BotCommand(command='photo', description='Sending photo'),
        BotCommand(command='video', description='Sending video'),
        BotCommand(command='voice', description='Sending voice_message')
    ]
    
    await bot.set_my_commands(commands, BotCommandScopeDefault())
    