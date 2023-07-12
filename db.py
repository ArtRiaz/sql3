import sqlite3 as sq

db = sq.connect("tb.db")
cur = db.cursor()


async def data_base():
    cur.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER)")

    db.commit()


async def user_id(message):
    cur.execute("INSERT INTO user (user_id) VALUES(?)", [message.chat.id])
