from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

delete = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="✔ Так",
                                             callback_data="yes_del"
                                         ),
                                         InlineKeyboardButton(
                                             text="❌ Ні",
                                             callback_data="no_del"
                                         ),
                                     ]
                                 ])