from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from keyboards.inline.delete_bot import delete
from states.create_bot import deleteBot
from loader import dp
from utils.db_api.dbconfig import get_bot_id, get_field, create_users_for_db, delete_bot
from bot_deployment.deployer import BotDeployer
from data.config import bot_deployer_connection_config


@dp.message_handler(Command("delete"))
async def bot_start(message: types.Message, state: FSMContext):
    bot = await get_bot_id(message.from_user.id)
    if bot != '':
        await message.answer("❗ Бажаєте видалити свого бота? ❗", reply_markup=delete)
        await deleteBot.delete.set()
        await state.update_data(user_id=message.from_user.id)
    else:
        await message.answer("🤷‍♂️ Ви поки що не створилит жодного бота.\nДля створення бота обреіть команду /creat_bot")



@dp.callback_query_handler(Text('yes_del'), state=deleteBot.delete)
async def cancel(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get("user_id")

    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("⚙ Видаляю бота...")
    bot = BotDeployer(bot_deployer_connection_config)
    bot_id = await get_bot_id(user_id)
    bot.remove(bot_id)
    username = await get_field('users', user_id, 'user', 'name')
    await create_users_for_db(id=user_id, username=username, phone='', bot_id="",
                              bot_name="", bot_token="")
    await delete_bot(bot_id)
    await call.message.answer("Ви видалили свого бота.")
    await state.finish()

@dp.callback_query_handler(Text('no_del'), state=deleteBot.delete)
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("Добре, що ви передумали 🙏🏻")
    await state.finish()
