from create_bot import dp, bot
from aiogram import types, Dispatcher


async def get_start(massege: types.Message):
    await bot.send_message(chat_id=massege.from_user.id, text="Hello my friend")
    db = sq.connect("tb.db")
    cur = db.cursor()
    cur.execute("INSERT INTO user (user_id) VALUES(?)", [message.chat.id])


async def get_inside(message: types.Message):
    db = sq.connect("tb.db")
    cur = db.cursor()
    user = cur.execute("SELECT * FROM user")
    print(user)

    await bot.send_message(chat_id=message.from_user.id, text=f'{user}')


def register_start(dp: Dispatcher):
    dp.register_message_handler(get_start, commands=["start"])
    dp.register_message_handler(get_inside, commands=["inside"])
