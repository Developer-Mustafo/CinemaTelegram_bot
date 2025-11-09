from aiogram import types, F, Router
from model import Film
from database import add_film
from config import ADMIN_ID

router = Router()

@router.message(F.video, ~F.chat.type == "private")
async def save_video(message: types.Message):
    caption = message.caption
    file_id = message.video.file_id
    film = Film(caption=caption, file_id=file_id)
    film_id = add_film(film)
    await message.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"🎬 Film muvoffaqiyatli yuklandi!\nFilm kodi: <code>{film_id}</code>",
        parse_mode="HTML"
    )