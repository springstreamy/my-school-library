import streamlit as st
from db.database import add_book_to_db

st.title("➕ Add Book")

book_title = st.text_input("Book Title")
book_author = st.text_input("Author")

if st.button("Add Book"):
    if book_title:
        add_book_to_db(book_title, book_author)
        st.success(f"Added '{book_title}' successfully!")
    else:
        st.error("Please enter a book title.")