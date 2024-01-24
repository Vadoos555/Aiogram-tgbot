from aiogram import Bot, Router
from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram.utils.chat_action import ChatActionSender
from aiogram.filters import Command


media_router = Router()


@media_router.message(Command('audio'))
async def send_audio(message: Message, bot: Bot):
    async with ChatActionSender.upload_document(bot, message.chat.id):
        audio_file = FSInputFile(path=r'C:\Users\User\Desktop\media\disco.mp3', filename='audiofile.mp3')
        await bot.send_audio(message.chat.id, audio=audio_file)


@media_router.message(Command('document'))
async def send_document(message: Message, bot: Bot):
    document = FSInputFile(path=r'C:\Users\User\Desktop\media\resume.docx', filename='cv.docx')
    await bot.send_document(message.chat.id, document=document, caption='Its document')
    

@media_router.message(Command('photo'))
async def send_photo(message: Message, bot: Bot):
    async with ChatActionSender.upload_photo(bot=bot, chat_id=message.chat.id):
        photo = FSInputFile(path=r'C:\Users\User\Desktop\media\hipos.jpg')
        await bot.send_photo(message.chat.id, photo=photo, caption='It is photo')


@media_router.message(Command('video'))
async def send_video(message: Message, bot: Bot):
    async with ChatActionSender.upload_video(bot=bot, chat_id=message.chat.id):
        video = FSInputFile(path=r'C:\Users\User\Desktop\media\robots.mp4')
        await bot.send_video(message.chat.id, video=video)


@media_router.message(Command('voice'))
async def send_voice(message: Message, bot: Bot):
    async with ChatActionSender.upload_voice(bot=bot, chat_id=message.chat.id):
        voice_file = FSInputFile(path=r'C:\Users\User\Desktop\media\voice.ogg')
        await bot.send_voice(message.chat.id, voice=voice_file)


@media_router.message(Command('mediagroup'))
async def send_mediagroup(message: Message, bot: Bot):
    photo1_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\User\Desktop\media\lion.jpg'),
                                caption='It is mediagroup')
    photo2_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\User\Desktop\media\hipos.jpg'))
    video_mg = InputMediaVideo(type='video', media=FSInputFile(r'C:\Users\User\Desktop\media\robots.mp4'))
    media = [photo1_mg, photo2_mg, video_mg]
    await bot.send_media_group(message.chat.id, media)
    