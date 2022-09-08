from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# you can configure more bot types here.
BOT_TEMPLATES = [
    {
        "button_text": "Створити Welcome Bot",
        "bot_id": "welcome_bot",
        "github_repo": "git@github.com:MrTuchka/Welcome_bot.git",
    }
]

cancel_button = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="❌ Відмінити",
                                             callback_data="cancel"
                                         ),
                                     ]
                                 ])

createuser = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f'🤖 {bot_template["button_text"]}',
                callback_data=f"create_bot__{bot_template['bot_id']}",
            ) for bot_template in BOT_TEMPLATES

        ],
        [
            InlineKeyboardButton(
                text="❌ Відмінити",
                callback_data="cancel",
            )

        ]
    ]
)
