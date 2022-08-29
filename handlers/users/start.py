from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from bot_deployment.deployer import BotDeployer
from data.config import bot_deployer_connection_config
from keyboards.inline.createuserbuttons import createuser, BOT_TEMPLATES
from loader import dp


def _get_bot_token() -> str:
    # todo: implement bot token functionality here
    return "5723874330:AAGwVIu3XPshR6H47kiR9XE9EgTYWFFbcV0"


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("To create your bot, tap the button", reply_markup=createuser)


@dp.callback_query_handler(Text(startswith="create_bot__"))
async def create_user(call: CallbackQuery):
    bot_id = call.data.split("__")[1]
    bot_template = next((t for t in BOT_TEMPLATES if t["bot_id"] == bot_id), None)
    if bot_template is None:
        await call.message.answer("Oops! no bots found.")
        return

    github_repo = bot_template["github_repo"]
    bot_token = _get_bot_token()

    await call.message.answer("Started deploying new bot. Please wait...")

    deployer = BotDeployer(bot_deployer_connection_config)
    deployment_id = deployer.deploy(github_repo, bot_token)

    await call.message.answer(f"New bot has been deployed with deployment id: {deployment_id}")
