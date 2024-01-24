from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from app.utils.states_form import StepsForm


form_router = Router()


@form_router.message(Command('form'))
async def get_form(message: types.Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name} starting to fill a form. Input your name')
    await state.set_state(StepsForm.GET_NAME)


@form_router.message(StepsForm.GET_NAME)
async def get_name(message: types.Message, state: FSMContext):
    await message.answer(f'Your name:\n{message.text}\n Input your surname:')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


@form_router.message(StepsForm.GET_LAST_NAME)
async def get_last_name(message: types.Message, state: FSMContext):
    await message.answer(f'Your surname\n {message.text}\n Input your age:')
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)


@form_router.message(StepsForm.GET_AGE)
async def get_age(message: types.Message, state: FSMContext):
    await message.answer(f'Your age:\n {message.text}')
    content_data = await state.get_data()
    await message.answer(f'Saved data in fsm\n {str(content_data)}')
    
    name = content_data.get('name')
    last_name = content_data.get('last_name')
    user_data = f'Here"s your data:\nName: <b>{name}</b>\nSurname: <b>{last_name}</b>\nAge: <b>{message.text}</b>'
    
    await message.answer(user_data)
    await state.clear()
    