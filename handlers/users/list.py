from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from utils.db_api.dbconfig import get_all_bots


@dp.message_handler(Command("list"))
async def bot_start(message: types.Message):
    list_bots = await get_all_bots()
    all_bot = []
    for bot in list_bots:
        if bot != '':
            all_bot.append("🤖 " + bot)
    text_bot = '\n'.join(all_bot)
    await message.answer(f'Список усіх зареєстрованих ботів\n**********\n{text_bot}')