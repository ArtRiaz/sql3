from create_bot import dp, bot
from aiogram import types, Dispatcher
from db import user_id


async def get_start(massege: types.Message):
    await bot.send_message(chat_id=massege.from_user.id, text="Hello my friend")
    await user_id(massege)


def register_start(dp: Dispatcher):
    dp.register_message_handler(get_start, commands=["start"])
