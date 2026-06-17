import sqlite3


def init_db():
    conn = sqlite3.connect("school_library.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            pages INTEGER
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS readers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT
        )
        """
    )
    conn.commit()


def add_book_to_db(title, author):
    # Connect again inside the function to ensure smooth updates
    db = sqlite3.connect("school_library.db")
    cur = db.cursor()
    cur.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)", (title, author)
    )
    db.commit()
    db.close()


def get_all_books():
    db = sqlite3.connect("school_library.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()
    db.close()
    return data