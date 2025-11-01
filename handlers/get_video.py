from aiogram import types, F, Router
from database import get_film

router = Router()

@router.message(F.text, F.chat.type.contains('private'))
async def get_video(message: types.Message):
    try:
        film_id = int(message.text)
        film = get_film(film_id)
        caption = (f'Film nomi: {film.title}\n'
                   f'Janri: {film.genre}\n'
                   f'Film yili: {film.year}\n')
        await message.bot.send_video(chat_id=message.chat.id, video=film.file_id, caption=caption)
    except ValueError:
        await message.answer('Bunday kino yo\'q')