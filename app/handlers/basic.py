from aiogram import Router, F, Bot
from aiogram import types
from aiogram.filters import CommandStart, Command

from app.keyboards.reply import reply_keyboard, phone_poll_keyboard, create_reply_keyboard
from app.keyboards.inline import select_macbook, get_inline_keyboard
from app.filters.is_contact import IsTrueContact

from app.middlewares.counter_mw import CounterMiddleware
from app.middlewares.officehours_mw import OfficeHoursMiddleware

from app.database.requests import set_user


basic_router = Router()

basic_router.message.middleware(CounterMiddleware())
basic_router.message.middleware(OfficeHoursMiddleware())


@basic_router.message(CommandStart())
async def get_start(message: types.Message, counter: str):
    await set_user(message.from_user.id, message.from_user.first_name)
    await message.answer(f'Message #{counter}')
    await message.answer(f'Hello <b>{message.from_user.first_name}</b> Glad to see you',
                         reply_markup=reply_keyboard)


@basic_router.message(Command('inline'))
async def get_inline(message: types.Message):
    await message.answer(f'Hi {message.from_user.first_name}. I show you inline buttons.',
                         reply_markup=get_inline_keyboard())


@basic_router.message(Command('help'))
async def make_help(message: types.Message):
    await message.answer(f'You need a help {message.from_user.first_name}? Send data for help',
                         reply_markup=create_reply_keyboard())


@basic_router.message(Command('reply'))
async def create_poll(message: types.Message):
    await message.answer(f'Send your data or create a poll {message.from_user.first_name}',
                         reply_markup=phone_poll_keyboard)


@basic_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f'You sent location\r\n'
                         f'{message.location.latitude}\r\n'
                         f'{message.location.longitude}')


@basic_router.message(F.photo)
async def get_photo(message: types.Message, bot: Bot):
    await message.answer(f'Great. You sent a picture, I save it.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


@basic_router.message(F.text.lower() == 'hello')
async def get_hello(message: types.Message):
    await message.answer(f'Hi! How are you?') 
    # json_str = json.dumps(message.dict(), default=str)
    # print(json_str) 


@basic_router.message(F.contact, IsTrueContact())
async def get_true_contact(message: types.Message, phone: str):
    await message.answer(f'You sent your contact {phone}')


@basic_router.message(F.contact)
async def get_fake_contact(message: types.Message):
    await message.answer(f'You sent fake contact')
