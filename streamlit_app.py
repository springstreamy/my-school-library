import sqlite3
import streamlit as st

# === 1. DATABASE SETUP (The Back) ===
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


# === 2. LOGIC FUNCTIONS (The Bridge) ===
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


# === 3. USER INTERFACE (The Front) ===
st.title("📚 Rambam School Library")

# Form to add data
st.subheader("Add a New Book")
book_title = st.text_input("Book Title")
book_author = st.text_input("Author")

if st.button("Add Book"):
    if book_title:  # Make sure they typed something
        add_book_to_db(book_title, book_author)
        st.success(f"Added '{book_title}' successfully!")
    else:
        st.error("Please enter a book title.")

# Live display of data
st.write("---")
st.subheader("Current Library Catalog")
books_list = get_all_books()

# Show the data in a neat table format
st.table(books_list)