from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api.dbconfig import add_statistics, create_users_for_db, chek_user
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    new_user = await chek_user(message.from_user.id)
    if new_user == True:
        await message.answer(f"Привіт 👋🏻, {message.from_user.full_name}.\nТи на шляху до створення свого першого бота.\nЩоб створити бота, обери команду /create_bot")
        await add_statistics()
        await create_users_for_db(id=message.from_user.id, username=message.from_user.full_name, phone='', bot_id='', bot_name='', bot_token='')
    else:
        await message.answer(f"Привіт 👋🏻, {message.from_user.full_name}.\nЗ поверненням!")