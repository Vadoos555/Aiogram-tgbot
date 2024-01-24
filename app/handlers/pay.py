from aiogram import Bot, Router, F

from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardMarkup, \
    InlineKeyboardButton, ShippingOption, ShippingQuery
from aiogram.filters import Command

from config import PAY_TOKEN


pay_router = Router()


keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='To pay an order', pay=True)],
    [InlineKeyboardButton(text='Link', url='https://example.com')]
])


UA_Shipping = ShippingOption(
    id='ua',
    title='Delivery to Ukraine',
    prices=[LabeledPrice(label='Ukrposhta', amount=2000)])

By_Shipping = ShippingOption(
    id='by',
    title='Delivery to Belorussia',
    prices=[LabeledPrice(label='Belposhta', amount=3000)])

CITIES_Shipping = ShippingOption(
    id='capitals',
    title='Fast delivery by city',
    prices=[LabeledPrice(label='Express delivery', amount=5000)])


@pay_router.shipping_query()
async def process_shipping(shiping_query: ShippingQuery, bot: Bot):
    shiping_options = []
    countries = ['UA', 'BY']
    
    if shiping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(shiping_query.id, ok=False,
                                               error_message='No delivering in this country')
    
    if shiping_query.shipping_address.country_code == 'BY':
        shiping_options.append(By_Shipping)
    
    if shiping_query.shipping_address.country_code == 'UA':
        shiping_options.append(UA_Shipping)
    
    cities = ['Kyiv', 'Minsk']
    if shiping_query.shipping_address.city in cities:
        shiping_options.append(CITIES_Shipping)
    
    await bot.answer_shipping_query(shiping_query.id, ok=True, shipping_options=shiping_options)


@pay_router.message(Command('pay'))
async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Purchase via Telegram bot',
        description='We learn to take payments through tg_bot',
        payload='Payment through a bot',
        provider_token=PAY_TOKEN,
        currency='UAH',
        prices=[
            LabeledPrice(label='Life training',amount=50000),
            LabeledPrice(label='ПДВ', amount=10000),
            LabeledPrice(label='discount',amount=-10000),
            LabeledPrice(label='bonus',amount=-8000),
            
        ],
         max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='Vadoos',
        provider_data=None,
        photo_url='https://i.ibb.co/zGw5X0B/image.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=True,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=25
    )


@pay_router.pre_checkout_query()
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@pay_router.message(F.successful_payment)
async def successful_payment(message: Message):
    msg = f'Thank for your payment {message.successful_payment.total_amount // 100} {message.successful_payment.currency}'
    await message.answer(msg)
    