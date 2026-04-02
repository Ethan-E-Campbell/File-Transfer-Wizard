"""
Codeunit: main_page.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Landing page for FTW app
"""
import streamlit as st


st.title("Welcome to File Transfer Wizard, also known as FTW.")
st.write("FTW is a PGP encryption tool, with support for SFTP file transfers.")
st.write("Please note! You must have GPG installed on your machine " +
         "to use this tool.")
st.write("Please select a page from the sidebar to get started.")

footer = st.container()
footer.divider()
footer.caption("Ethan Campbell, 2026")
