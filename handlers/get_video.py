from aiogram import types, F, Router
from database import get_film, delete_film

router = Router()

@router.message(F.text, F.chat.type.contains('private'))
async def get_video(message: types.Message):
    try:
        film_id = int(message.text)
        film = get_film(film_id)
        if film is not None:
            await message.bot.send_video(chat_id=message.chat.id, video=film.file_id, caption=film.caption)
        else:
            await message.answer('Bunday film yo\'q')
    except AttributeError:
        film_id = int(message.text)
        delete_film(film_id)