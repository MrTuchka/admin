from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from states.edit_bot import edit_bott

from keyboards.inline.edit import edit_bot_buttons
from loader import dp
from utils.db_api.dbconfig import get_bot_id, get, get_button, get_button_ref, edit_bot, get_main


#Редагування привітального тексту
@dp.message_handler(Command("edit"))
async def edit(message: types.Message):
    bot = await get_bot_id(message.from_user.id)
    if bot != '' and bot != "No data":
        bot_id = await get_bot_id(message.from_user.id)
        main = await get("bots", bot_id, "main")

        button1 = await get_button(bot_id, "1")
        ref1 = await get_button_ref(bot_id, "1")

        button2 = await get_button(bot_id, "2")
        ref2 = await get_button_ref(bot_id, "2")

        button3 = await get_button(bot_id, "3")
        ref3 = await get_button_ref(bot_id, "3")

        button4 = await get_button(bot_id, "4")
        ref4 = await get_button_ref(bot_id, "4")

        button5 = await get_button(bot_id, "5")
        ref5 = await get_button_ref(bot_id, "5")

        await message.answer(f"Ваш бот виглядає так:\n\n"
                             f"<b>Привітальне повідомлення:</b> {main}\n\n"
                             f"<b>Кнопка 1:</b> {button1}\n"
                             f"<b>Посилання:</b> {ref1}\n\n"
                             f"<b>Кнопка 2:</b> {button2}\n"
                             f"<b>Посилання:</b> {ref2}\n\n"
                             f"<b>Кнопка 3:</b> {button3}\n"
                             f"<b>Посилання:</b> {ref3}\n\n"
                             f"<b>Кнопка 4:</b> {button4}\n"
                             f"<b>Посилання:</b> {ref4}\n\n"
                             f"<b>Кнопка 5:</b> {button5}\n"
                             f"<b>Посилання:</b> {ref5}\n\n", parse_mode="html", reply_markup=edit_bot_buttons)
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")


@dp.callback_query_handler(Text('edit_main_text'))
async def edit_main(call: CallbackQuery, state: FSMContext):
    bot = await get_bot_id(call.message.chat.id)
    if bot != '' and bot != "No data":
        await call.message.answer("Відправте ваш текст для редагування опису.")
        await edit_bott.main.set()
        await state.update_data(message_id=call.message.message_id)
    else:
        await call.message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.main)
async def edit_main_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_to_edit_id = data.get("message_id")

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data":
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, message.text, b1, r1, b2, r2, b3, r3, b4, r4, b5, r5)

        await dp.bot.edit_message_text(message_id=message_to_edit_id, chat_id=message.from_user.id,
                                       text=f"Ваш бот виглядає так:\n\n"
                                            f"<b>Привітальне повідомлення:</b> {message.text}\n\n"
                                            f"<b>Кнопка 1:</b> {b1}\n"
                                            f"<b>Посилання:</b> {r1}\n\n"
                                            f"<b>Кнопка 2:</b> {b2}\n"
                                            f"<b>Посилання:</b> {r2}\n\n"
                                            f"<b>Кнопка 3:</b> {b3}\n"
                                            f"<b>Посилання:</b> {r3}\n\n"
                                            f"<b>Кнопка 4:</b> {b4}\n"
                                            f"<b>Посилання:</b> {r4}\n\n"
                                            f"<b>Кнопка 5:</b> {b5}\n"
                                            f"<b>Посилання:</b> {r5}\n\n", parse_mode="html",
                                       reply_markup=edit_bot_buttons)

        await state.finish()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")


#Редагування кнопки1
@dp.callback_query_handler(Text('b1'))
async def edit_b1(call: CallbackQuery, state: FSMContext):
    bot = await get_bot_id(call.message.chat.id)
    if bot != '' and bot != "No data":
        await call.message.answer("Відправте ваш текст для редагування кнопки 1.\nАбо відправте 🚫, для видалення кнопки.")
        await edit_bott.b1.set()
        await state.update_data(message_id=call.message.message_id)
    else:
        await call.message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.b1)
async def edit_button1(message: types.Message):

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data":
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, message.text, r1, b2, r2, b3, r3, b4, r4, b5, r5)

        await message.answer("Тепер введіть посилання\n<i>(посилання має починатися з hhtps:// або http://)</i>\nАбо відправте 🚫, для видалення посилання.", parse_mode="html")
        await edit_bott.r1.set()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.r1)
async def edit_ref1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_to_edit_id = data.get("message_id")

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data" and (message.text.startswith("https://") or message.text.startswith("http://") or message.text == "🚫"):
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, message.text, b2, r2, b3, r3, b4, r4, b5, r5)

        await dp.bot.edit_message_text(message_id=message_to_edit_id, chat_id=message.from_user.id,
                                       text=f"Ваш бот виглядає так:\n\n"
                                            f"<b>Привітальне повідомлення:</b> {main}\n\n"
                                            f"<b>Кнопка 1:</b> {b1}\n"
                                            f"<b>Посилання:</b> {message.text}\n\n"
                                            f"<b>Кнопка 2:</b> {b2}\n"
                                            f"<b>Посилання:</b> {r2}\n\n"
                                            f"<b>Кнопка 3:</b> {b3}\n"
                                            f"<b>Посилання:</b> {r3}\n\n"
                                            f"<b>Кнопка 4:</b> {b4}\n"
                                            f"<b>Посилання:</b> {r4}\n\n"
                                            f"<b>Кнопка 5:</b> {b5}\n"
                                            f"<b>Посилання:</b> {r5}\n\n", parse_mode="html",
                                       reply_markup=edit_bot_buttons)

        await state.finish()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного або ввели неправильне посилання.❗\nСтвроти бота /create_bot")

#Редагування кнопки2
@dp.callback_query_handler(Text('b2'))
async def edit_b2(call: CallbackQuery, state: FSMContext):
    bot = await get_bot_id(call.message.chat.id)
    if bot != '' and bot != "No data":
        await call.message.answer("Відправте ваш текст для редагування кнопки 2.\nАбо відправте 🚫, для видалення кнопки.")
        await edit_bott.b2.set()
        await state.update_data(message_id=call.message.message_id)
    else:
        await call.message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.b2)
async def edit_button2(message: types.Message):

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data":
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, r1, message.text, r2, b3, r3, b4, r4, b5, r5)

        await message.answer("Тепер введіть посилання\n<i>(посилання має починатися з hhtps:// або http://)</i>\nАбо відправте 🚫, для видалення посилання.", parse_mode="html")
        await edit_bott.r2.set()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.r2)
async def edit_ref2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_to_edit_id = data.get("message_id")

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data" and (message.text.startswith("https://") or message.text.startswith("http://") or message.text == "🚫"):
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, r2, b2, message.text, b3, r3, b4, r4, b5, r5)

        await dp.bot.edit_message_text(message_id=message_to_edit_id, chat_id=message.from_user.id,
                                       text=f"Ваш бот виглядає так:\n\n"
                                            f"<b>Привітальне повідомлення:</b> {main}\n\n"
                                            f"<b>Кнопка 1:</b> {b1}\n"
                                            f"<b>Посилання:</b> {r1}\n\n"
                                            f"<b>Кнопка 2:</b> {b2}\n"
                                            f"<b>Посилання:</b> {message.text}\n\n"
                                            f"<b>Кнопка 3:</b> {b3}\n"
                                            f"<b>Посилання:</b> {r3}\n\n"
                                            f"<b>Кнопка 4:</b> {b4}\n"
                                            f"<b>Посилання:</b> {r4}\n\n"
                                            f"<b>Кнопка 5:</b> {b5}\n"
                                            f"<b>Посилання:</b> {r5}\n\n", parse_mode="html",
                                       reply_markup=edit_bot_buttons)

        await state.finish()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

#Редагування кнопки3
@dp.callback_query_handler(Text('b3'))
async def edit_b3(call: CallbackQuery, state: FSMContext):
    bot = await get_bot_id(call.message.chat.id)
    if bot != '' and bot != "No data":
        await call.message.answer("Відправте ваш текст для редагування кнопки 3.\nАбо відправте 🚫, для видалення кнопки.")
        await edit_bott.b3.set()
        await state.update_data(message_id=call.message.message_id)
    else:
        await call.message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.b3)
async def edit_button3(message: types.Message):

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data":
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, r1, b2, r2, message.text, r3, b4, r4, b5, r5)

        await message.answer("Тепер введіть посилання\n<i>(посилання має починатися з hhtps:// або http://)</i>\nАбо відправте 🚫, для видалення посилання.", parse_mode="html")
        await edit_bott.r3.set()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.r3)
async def edit_ref3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_to_edit_id = data.get("message_id")

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data" and (message.text.startswith("https://") or message.text.startswith("http://") or message.text == "🚫"):
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, r2, b2, r2, b3, message.text, b4, r4, b5, r5)

        await dp.bot.edit_message_text(message_id=message_to_edit_id, chat_id=message.from_user.id,
                                       text=f"Ваш бот виглядає так:\n\n"
                                            f"<b>Привітальне повідомлення:</b> {main}\n\n"
                                            f"<b>Кнопка 1:</b> {b1}\n"
                                            f"<b>Посилання:</b> {r1}\n\n"
                                            f"<b>Кнопка 2:</b> {b2}\n"
                                            f"<b>Посилання:</b> {r2}\n\n"
                                            f"<b>Кнопка 3:</b> {b3}\n"
                                            f"<b>Посилання:</b> {message.text}\n\n"
                                            f"<b>Кнопка 4:</b> {b4}\n"
                                            f"<b>Посилання:</b> {r4}\n\n"
                                            f"<b>Кнопка 5:</b> {b5}\n"
                                            f"<b>Посилання:</b> {r5}\n\n", parse_mode="html",
                                       reply_markup=edit_bot_buttons)

        await state.finish()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")


#Редагування кнопки4
@dp.callback_query_handler(Text('b4'))
async def edit_b4(call: CallbackQuery, state: FSMContext):
    bot = await get_bot_id(call.message.chat.id)
    if bot != '' and bot != "No data":
        await call.message.answer("Відправте ваш текст для редагування кнопки 4.\nАбо відправте 🚫, для видалення кнопки.")
        await edit_bott.b4.set()
        await state.update_data(message_id=call.message.message_id)
    else:
        await call.message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.b4)
async def edit_button4(message: types.Message):

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data":
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, r1, b2, r2, b3, r3, message.text, r4, b5, r5)

        await message.answer("Тепер введіть посилання\n<i>(посилання має починатися з hhtps:// або http://)</i>\nАбо відправте 🚫, для видалення посилання.", parse_mode="html")
        await edit_bott.r4.set()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.r4)
async def edit_ref4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_to_edit_id = data.get("message_id")

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data" and (message.text.startswith("https://") or message.text.startswith("http://") or message.text == "🚫"):
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, r2, b2, r2, b3, r3, b4, message.text, b5, r5)

        await dp.bot.edit_message_text(message_id=message_to_edit_id, chat_id=message.from_user.id,
                                       text=f"Ваш бот виглядає так:\n\n"
                                            f"<b>Привітальне повідомлення:</b> {main}\n\n"
                                            f"<b>Кнопка 1:</b> {b1}\n"
                                            f"<b>Посилання:</b> {r1}\n\n"
                                            f"<b>Кнопка 2:</b> {b2}\n"
                                            f"<b>Посилання:</b> {r2}\n\n"
                                            f"<b>Кнопка 3:</b> {b3}\n"
                                            f"<b>Посилання:</b> {r3}\n\n"
                                            f"<b>Кнопка 4:</b> {b4}\n"
                                            f"<b>Посилання:</b> {message.text}\n\n"
                                            f"<b>Кнопка 5:</b> {b5}\n"
                                            f"<b>Посилання:</b> {r5}\n\n", parse_mode="html",
                                       reply_markup=edit_bot_buttons)

        await state.finish()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")


#Редагування кнопки5
@dp.callback_query_handler(Text('b5'))
async def edit_b4(call: CallbackQuery, state: FSMContext):
    bot = await get_bot_id(call.message.chat.id)
    if bot != '' and bot != "No data":
        await call.message.answer("Відправте ваш текст для редагування кнопки 5.\nАбо відправте 🚫, для видалення кнопки.")
        await edit_bott.b5.set()
        await state.update_data(message_id=call.message.message_id)
    else:
        await call.message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.b5)
async def edit_button5(message: types.Message):

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data":
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, r1, b2, r2, b3, r3, b4, r4, message.text, r5)

        await message.answer("Тепер введіть посилання\n<i>(посилання має починатися з hhtps:// або http://)</i>\nАбо відправте 🚫, для видалення посилання.", parse_mode="html")
        await edit_bott.r5.set()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")

@dp.message_handler(state=edit_bott.r5)
async def edit_ref5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_to_edit_id = data.get("message_id")

    bot = await get_bot_id(message.chat.id)
    if bot != '' and bot != "No data" and (message.text.startswith("https://") or message.text.startswith("http://") or message.text == "🚫"):
        try:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        except:
            pass

        try:
            await message.delete()
        except:
            pass
        bot_id = await get_bot_id(message.from_user.id)

        main = await get_main(bot_id)

        b1 = await get_button(bot_id, "1")
        r1 = await get_button_ref(bot_id, "1")

        b2 = await get_button(bot_id, "2")
        r2 = await get_button_ref(bot_id, "2")

        b3 = await get_button(bot_id, "3")
        r3 = await get_button_ref(bot_id, "3")

        b4 = await get_button(bot_id, "4")
        r4 = await get_button_ref(bot_id, "4")

        b5 = await get_button(bot_id, "5")
        r5 = await get_button_ref(bot_id, "5")

        await edit_bot(bot_id, main, b1, r2, b2, r2, b3, r3, b4, r4, b5, message.text)

        await dp.bot.edit_message_text(message_id=message_to_edit_id, chat_id=message.from_user.id,
                                       text=f"Ваш бот виглядає так:\n\n"
                                            f"<b>Привітальне повідомлення:</b> {main}\n\n"
                                            f"<b>Кнопка 1:</b> {b1}\n"
                                            f"<b>Посилання:</b> {r1}\n\n"
                                            f"<b>Кнопка 2:</b> {b2}\n"
                                            f"<b>Посилання:</b> {r2}\n\n"
                                            f"<b>Кнопка 3:</b> {b3}\n"
                                            f"<b>Посилання:</b> {r3}\n\n"
                                            f"<b>Кнопка 4:</b> {b4}\n"
                                            f"<b>Посилання:</b> {r4}\n\n"
                                            f"<b>Кнопка 5:</b> {b5}\n"
                                            f"<b>Посилання:</b> {message.text}\n\n", parse_mode="html",
                                       reply_markup=edit_bot_buttons)

        await state.finish()
    else:
        await message.answer("❗Ви ще не створили свого бота або видалили створеного❗\nСтвроти бота /create_bot")