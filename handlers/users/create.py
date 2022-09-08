from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from bot_deployment.deployer import BotDeployer
from data.config import bot_deployer_connection_config
from states.create_bot import createBot
from keyboards.inline.createuserbuttons import createuser, BOT_TEMPLATES, cancel_button
from loader import dp
from utils.db_api.dbconfig import get_bot_id, get_field, create_users_for_db


@dp.message_handler(Command("create_bot"))
async def bot_start(message: types.Message, state: FSMContext):
    try:

        for chat_message in range(3):
            await dp.bot.delete_message(message.chat.id, message.message_id - chat_message)
    except:
        pass
    bot = await get_bot_id(message.from_user.id)
    if bot == "No data":
        await message.answer("Для створення бота, надішліть токен, який ви можете отримати в @BotFather\n<a href='https://telegra.ph/YAk-otrimati-TOKEN-v-BotFather-09-02'>Інструкція</a> по отриманню ТОКЕНА.", reply_markup=cancel_button, disable_web_page_preview=True)
        await createBot.create.set()
    elif bot != '':
        await message.answer("🤷‍♂️ Ви не можете створити більше одного тестового бота.\nВидаліть свого бота, щоб створити нового натиснувши /delete")
    else:
        await message.answer("Для створення бота, надішліть токен, який ви можете отримати в @BotFather.\n<a href='https://telegra.ph/YAk-otrimati-TOKEN-v-BotFather-09-02'>Інструкція</a> по отриманню ТОКЕНА.", reply_markup=cancel_button, disable_web_page_preview=True)
        await createBot.create.set()
        await state.update_data(chat_id=message.chat.id, message_id=message.message_id)


@dp.message_handler(content_types=types.ContentType.ANY, state=createBot.create)
async def take_bot_token(message: types.Message, state: FSMContext):
    token = message.text
    user_id = message.from_user.id
    await state.update_data(Token=token, user_id=user_id)
    data = await state.get_data()
    chat_id = data.get("chat_id")
    message_id = data.get("message_id")
    await message.delete()
    try:
        if message.text[10] == ":" and len(message.text) == 46:
            await dp.bot.edit_message_text(chat_id=chat_id, message_id=(message_id + 1), text=f"Створити бота з токеном:\n--------\n<b>{message.text}</b>"
                                                                                        f"\n--------\n<i>Якщо ви не вірно ввели токен, просто "
                                                                                        f"відправте новий</i>", reply_markup=createuser, parse_mode="html")
            await createBot.create.set()
    except:
        try:
            await dp.bot.delete_message(message.chat.id, message.message_id - 1)
            await message.delete()
        except:
            pass

        await message.answer(
            "❗Ви ввели не вірний ТОКЕН❗\nПерейдіть в @BotFather та зкопіюйте ТОКЕН, якщо ви вже створили бота.\n\nАбо спочатку створіть бота в @BotFather, а вже потім скопіюйте токен.\n\nПісля отримання ТОКЕНА повертайтесь і натисніть /create_bot")
        await state.finish()

@dp.callback_query_handler(Text('cancel'), state=createBot.create)
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("Якщо, передумаєте, просто натисніть команду /create_bot")
    await state.finish()



@dp.callback_query_handler(Text(startswith="create_bot__"), state=createBot.create)
async def create_user(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = data.get("Token")

    data = await state.get_data()
    user_id = data.get("user_id")
    username = await get_field('users', user_id, 'user', 'name')

    bot_id = call.data.split("__")[1]
    bot_template = next((t for t in BOT_TEMPLATES if t["bot_id"] == bot_id), None)
    if bot_template is None:
        await call.message.answer("❗ Oops! Ботів не знайдено ❗")
        await state.finish()
        return

    github_repo = bot_template["github_repo"]
    bot_token = str(token)

    await call.message.delete()
    await call.message.answer("⚙ Створюю бота, будь-ласка зачекайте...")

    deployer = BotDeployer(bot_deployer_connection_config)
    deployment_id = deployer.deploy(github_repo, bot_token, user_id)

    await create_users_for_db(id=user_id, username=username, phone='', bot_id=deployment_id,
                              bot_name=bot_id, bot_token=bot_token)

    await call.message.answer(f"Ваш бот створено.\n"
                              f"Для налаштування бота натисніть /edit")
    await state.finish()
