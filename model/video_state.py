from aiogram.fsm.state import State, StatesGroup

class VideoState(StatesGroup):
    video = State()
    title = State()
    genre = State()
    year = State()