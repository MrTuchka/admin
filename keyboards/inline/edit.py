from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


edit_bot_buttons = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f'📝 Редагувати опис',
                callback_data="edit_main_text",
            ),
            InlineKeyboardButton(
                text=f'🔘 Кнопка 1',
                callback_data="b1",
            ),

        ],
        [
            InlineKeyboardButton(
                text=f'🔘 Кнопка 2',
                callback_data="b2",
            ),
            InlineKeyboardButton(
                text=f'🔘 Кнопка 3',
                callback_data="b3",
            ),

        ],
        [
            InlineKeyboardButton(
                text=f'🔘 Кнопка 4',
                callback_data="b4",
            ),
            InlineKeyboardButton(
                text=f'🔘 Кнопка 5',
                callback_data="b5",
            ),

        ]
    ]
)

