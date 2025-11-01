from aiogram.filters import CommandStart
from aiogram import types, Router
from model import User
from database import add_user
router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    first_name = message.from_user.first_name or ''
    last_name = message.from_user.last_name or ''
    telegram_id = message.from_user.id
    user = User(telegram_id, first_name, last_name)
    add_user(user)
    await message.answer(f'Assalomu aleykum {message.from_user.first_name}, {message.from_user.last_name}')