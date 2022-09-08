from aiogram import types
from aiogram.types import BotCommandScopeChat

from data.config import ADMINS
from utils.db_api.environments_for_db import db


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "✔ запустити"),
            types.BotCommand("create_bot", "🤖 створити власного бота"),
            types.BotCommand("edit", "📝 редагувати бота"),
            types.BotCommand("delete", "❌ видалити бота"),
        ]
    )

#Команди, які бачать тільки адмінітсратори
    for admin in ADMINS:
        await dp.bot.set_my_commands(
        [
            types.BotCommand("create_bot", "🤖 створити власного бота"),
            types.BotCommand("send", "💬 розсилка повідомлень"),
            types.BotCommand("list", "📑 список ботів"),
            types.BotCommand("edit", "📝 редагувати бота"),
            types.BotCommand("delete", "❌ видалити бота"),
        ], BotCommandScopeChat(chat_id=admin)
    )