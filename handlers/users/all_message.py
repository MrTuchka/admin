from aiogram import types
from loader import dp


@dp.message_handler()
async def all_message(message: types.Message):
    await message.delete()