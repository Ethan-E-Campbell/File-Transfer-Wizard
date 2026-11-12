"""
Codeunit: filewatch_page.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Frontend page.
Monitor for files and encrypt / send them automatically
"""

import streamlit as st
from backend.filewatch_db import initiate_database as initiate_database
conn = initiate_database()
print(conn)
st.write("Welcome to the file watch page!")

st.write("Please provide the following information.")

file_path = st.text_input("Please provide the file path of the directory you would like to monitor.")
pgp_or_not = st.selectbox("Would you like to use PGP encryption?", ["Yes", "No"], index=0)
if pgp_or_not == "Yes":
    pgp_key_selected = st.text_input("Please provide the PGP key you would like to use for encryption.")

cron_expression = st.text_input("Please provide the cron expression for the file monitoring schedule.")
