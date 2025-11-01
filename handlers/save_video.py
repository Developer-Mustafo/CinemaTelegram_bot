from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from model import VideoState, Film
from database import add_film
router = Router()

@router.message(F.video, F.chat.type.in_({'supergroup', 'group'}))
async def save_video(message: types.Message, state: FSMContext):
    print(type(message.video.file_id))
    await state.update_data(video=message.video.file_id)
    await state.set_state(VideoState.title)
    await message.answer('Film nomini yuboring:')

@router.message(VideoState.title, F.chat.type.in_({'supergroup', 'group'}))
async def save_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(VideoState.genre)
    await message.answer('Film janrini yuboring:')

@router.message(VideoState.genre, F.chat.type.in_({'supergroup', 'group'}))
async def save_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(VideoState.year)
    await message.answer('Film yilini yuboring:')

@router.message(VideoState.year, F.chat.type.in_({'supergroup', 'group'}))
async def save_year(message: types.Message, state: FSMContext):
    await state.update_data(year=message.text)

    data = await state.get_data()

    video=data.get("video")
    title=data.get("title")
    genre=data.get("genre")
    year=data.get("year")
    film = Film(title, year, genre, video)
    add_film(film)


    await message.answer("✅ Film muvaffaqiyatli saqlandi!")

    await state.clear()