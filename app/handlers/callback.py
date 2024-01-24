from aiogram.types import CallbackQuery
from aiogram import Router, F

from app.utils.call_back_data import MacInfo


callback_router = Router()


@callback_router.callback_query(MacInfo.filter(F.model == 'pro'))
async def select_macbook(call: CallbackQuery, callback_data: MacInfo):
    model = callback_data.model
    size = callback_data.size
    chip = callback_data.chip
    year = callback_data.year
    
    answer = f'{call.message.from_user.first_name}, you chose Apple Macbook {model}' \
             f' with size {size}, chip {chip} and year {year}'
    await call.message.answer(answer)
    await call.answer()  


# @callback_router.callback_query(F.data.startswith('apple_'))
# async def select_macbook(call: CallbackQuery):
#     model = call.data.split('_')[1]
#     size = call.data.split('_')[2]
#     chip = call.data.split('_')[3]
#     year = call.data.split('_')[4]
    
#     answer = f'{call.message.from_user.first_name}, you chose Apple Macbook {model}' \
#              f' with size {size}, chip {chip} and year {year}'
#     await call.message.answer(answer)
#     await call.answer()  
        