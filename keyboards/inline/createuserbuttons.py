from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

createuser = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Create",
                                             callback_data="create"
                                         ),
                                     ]
                                 ])