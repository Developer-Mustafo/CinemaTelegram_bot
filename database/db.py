import sqlite3
from model import User, Film

db = sqlite3.connect('./database/kinomania.db', check_same_thread=False)
cursor = db.cursor()


def create_tables():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user(
                user_id INTEGER NOT NULL UNIQUE,
                name TEXT NOT NULL,
                surname TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS film(
                film_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                caption TEXT NOT NULL,
                file_id TEXT NOT NULL
            )
        ''')
        db.commit()
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")


def add_user(user: User):
    try:
        cursor.execute("SELECT 1 FROM user WHERE user_id = ?", (user.user_id,))
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO user (user_id, name, surname) VALUES (?, ?, ?)",
                (user.user_id, user.name.strip(), user.surname.strip())
            )
        else:
            cursor.execute(
                "UPDATE user SET name = ?, surname = ? WHERE user_id = ?",
                (user.name.strip(), user.surname.strip(), user.user_id)
            )
        db.commit()
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")


def add_film(film: Film):
    caption = film.caption if film.caption is not None else ""
    try:
        cursor.execute(
            "INSERT INTO film (caption, file_id) VALUES (?, ?)",
            (caption.strip(), film.file_id.strip() if film.file_id else None)
        )
        db.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")

def update_user(user: User):
    if user.user_id is None:
        print("Error: user_id is required for update")
        return

    fields = []
    values = []
    if user.name is not None:
        fields.append("name = ?")
        values.append(user.name.strip())
    if user.surname is not None:
        fields.append("surname = ?")
        values.append(user.surname.strip())

    try:
        if fields:
            values.append(user.user_id)
            sql = f'UPDATE user SET {", ".join(fields)} WHERE user_id = ?'
            cursor.execute(sql, values)
            db.commit()
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")


def update_film(film: Film):
    if film.film_id is None:
        print("Error: film_id is required for update")
        return

    fields = []
    values = []
    if film.caption is not None:
        fields.append("caption = ?")
        values.append(film.caption.strip())
    if film.file_id is not None:
        fields.append("file_id = ?")
        values.append(film.file_id.strip())

    try:
        if fields:
            values.append(film.film_id)
            sql = f"UPDATE film SET {', '.join(fields)} WHERE film_id = ?"
            cursor.execute(sql, values)
            db.commit()
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")


def delete_user(user_id):
    try:
        cursor.execute("DELETE FROM user WHERE user_id = ?", (user_id,))
        db.commit()
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")


def delete_film(film_id):
    try:
        cursor.execute("DELETE FROM film WHERE film_id = ?", (film_id,))
        db.commit()
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")


def get_user(user_id: int) -> User | None:
    try:
        cursor.execute("SELECT user_id, name, surname FROM user WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            user_id, name, surname = row
            return User(
                user_id=user_id,
                name=str(name).strip() if name else "",
                surname=str(surname).strip() if surname else ""
            )
        return None
    except sqlite3.Error as e:
        print(f"SQLite Error (get_user): {e}")
        return None


def get_film(film_id: int) -> Film | None:
    try:
        cursor.execute("SELECT film_id, caption, file_id FROM film WHERE film_id = ?", (film_id,))
        row = cursor.fetchone()
        if row:
            film_id, caption, file_id = row
            return Film(
                film_id=film_id,
                caption=str(caption).strip() if caption else "",
                file_id=str(file_id).strip() if file_id else ""
            )
        return None
    except sqlite3.Error as e:
        print(f"SQLite Error (get_film): {e}")
        return None


def get_all_films() -> list[Film]:
    try:
        cursor.execute("SELECT film_id, title, year, genre, file_id FROM film")
        rows = cursor.fetchall()
        films = []
        for row in rows:
            film_id, caption, file_id = row
            films.append(Film(
                film_id=film_id,
                caption= caption,
                file_id=str(file_id).strip() if file_id else ""
            ))
        return films
    except sqlite3.Error as e:
        print(f"SQLite Error (get_all_films): {e}")
        return []


def close_connection():
    cursor.close()
    db.close()