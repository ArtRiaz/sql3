from create_bot import dp, bot
#from handlers import start
from db import data_base
from aiogram import types, executor


async def on_startup(_):
    await data_base()
    print("Бот запущен")



#start.register_handlers_start(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
