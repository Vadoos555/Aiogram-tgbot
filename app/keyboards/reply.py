from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Row 1. Button 1'),
        KeyboardButton(text='Row 1. Button 2'),
        KeyboardButton(text='Row 1. Button 3'),
    ],
    [
        KeyboardButton(text='Row 2. Button 1'),
        KeyboardButton(text='Row 2. Button 2'),
        KeyboardButton(text='Row 2. Button 3'),
        KeyboardButton(text='Row 2. Button 4')
    ],
     [
        KeyboardButton(text='Row 3. Button 1'),
        KeyboardButton(text='Row 3. Button 2'),
    ],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose the button.')


phone_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Send geolocation', request_location=True)],
    [KeyboardButton(text='Send your contact', request_contact=True)],
    [KeyboardButton(text='Create quiz', request_poll=KeyboardButtonPollType())]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Send location, phone or create poll.')


def create_reply_keyboard():
    kb_builder = ReplyKeyboardBuilder()
    
    kb_builder.button(text='Button 1')
    kb_builder.button(text='Button 2')
    kb_builder.button(text='Button 3')
    kb_builder.button(text='Send geo', request_location=True)
    kb_builder.button(text='Send contact', request_contact=True)
    kb_builder.button(text='Create poll', request_poll=KeyboardButtonPollType())
    kb_builder.adjust(3, 2, 1)
    
    return kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Send location, phone or create poll.')
    