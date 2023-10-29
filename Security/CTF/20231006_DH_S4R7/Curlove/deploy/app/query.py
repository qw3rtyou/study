from connections import connect_mysql
from threading import RLock

lock = RLock()
db, cursor = connect_mysql()


def get_user(username, password):
    try:
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        with lock:
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            if user:
                return user
    except Exception as e:
        print(e)
        db.close()


def register_user(username, password):
    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        with lock:
            cursor.execute(query, (username, password))
            db.commit()

    except Exception as e:
        print(e)
        db.close()
