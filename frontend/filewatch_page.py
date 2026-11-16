"""
Codeunit: filewatch_page.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Frontend page.
Monitor for files and encrypt / send them automatically
"""

import streamlit as st
# from backend.filewatch_db import initiate_database as initiate_database
from backend.filewatch_db import retrieve_file_watch_data as retrieve_file_watch_data
from backend.filewatch_db import insert_file_watch_data as insert_file_watch_data
from backend.filewatch_db import create_table as create_table


st.write("Welcome to the file watch page!")
create_table()
insert_file_watch_data("test_path", "test_key", "test_cron")
file_watch_data = retrieve_file_watch_data()
print(file_watch_data)

st.write("Please provide the following information.")

file_path = st.text_input("Please provide the file path of the directory you would like to monitor.")
pgp_or_not = st.selectbox("Would you like to use PGP encryption?", ["Yes", "No"], index=0)
if pgp_or_not == "Yes":
    pgp_key_selected = st.text_input("Please provide the PGP key you would like to use for encryption.")

cron_expression = st.text_input("Please provide the cron expression for the file monitoring schedule.")
