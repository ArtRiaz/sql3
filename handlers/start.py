from create_bot import dp, bot
from aiogram import types, Dispatcher
import sqlite3 as sq
from db import add_user, user


async def get_start(message: types.Message):
    await add_user(message.from_user.id)
    hell = await user()
    await bot.send_message(chat_id=message.from_user.id, text=f"Hello my friend{hell}")



def register_start(dp: Dispatcher):
    dp.register_message_handler(get_start, commands=["start"])

