import streamlit as st
import db.database


db.database.init_db()

home = st.Page("pages/home.py", title="Home", icon="🏠")
add_book = st.Page("pages/add_book.py", title="Add Book", icon="➕")
#catalog = st.Page("pages/catalog.py", title="Catalog", icon="📚")

pg = st.navigation([home, add_book])
pg.run()