from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# you can configure more bot types here.
BOT_TEMPLATES = [
    {
        "button_text": "Create Support Bot",
        "bot_id": "support_bot",
        "github_repo": "git@github.com:MrTuchka/support-bot.git",
    }
]

createuser = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=bot_template["button_text"],
                callback_data=f"create_bot__{bot_template['bot_id']}",
            ) for bot_template in BOT_TEMPLATES
        ]
    ]
)
