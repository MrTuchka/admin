from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline.createuserbuttons import createuser

from loader import dp



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("To create your bot, tap the button", reply_markup=createuser)

@dp.callback_query_handler(text='create')
async def create_user(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer("You create new bot")