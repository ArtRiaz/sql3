import sqlite3 as sq

db = sq.connect("tb.db")
cur = db.cursor()


async def data_base():
    cur.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER)")

    db.commit()


async def add_user(user_id):
    user = cur.execute("SELECT * FROM user WHERE user_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO user(user_id)  VALUES({key})".format(key=user_id))

        db.commit()

async def user():
    users = cur.execute("SELECT user_id FROM user").fetchone()
    print(users)
    return users
