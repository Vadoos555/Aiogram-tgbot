from aiogram.filters import BaseFilter
from aiogram import types


class IsTrueContact(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        if message.contact.user_id == message.from_user.id:
            return {'phone': message.contact.phone_number}
        else:
            return False
