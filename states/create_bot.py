from aiogram.dispatcher.filters.state import StatesGroup, State


class createBot(StatesGroup):
    create = State()

class support(StatesGroup):
    send_message = State()

class list(StatesGroup):
    listBots = State()

class deleteBot(StatesGroup):
    delete = State()
