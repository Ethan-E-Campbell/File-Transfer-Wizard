"""
Codeunit: filewatch_page.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Frontend page.
Monitor for files and encrypt / send them automatically
"""

import streamlit as st
from backend.filewatch_db import insert_file_watch_data as insert_file_watch_data
from backend.filewatch_db import create_table as create_table


st.write("Welcome to the file watch page!")
create_table()

st.write("Please provide the following information.")

file_path = st.text_input("Please provide the file path of the directory you would like to monitor.")
pgp_or_not = st.selectbox("Would you like to use PGP encryption?", ["Yes", "No"], index=0)
if pgp_or_not == "Yes":
    pgp_key_selected = st.text_input("Please provide the PGP key you would like to use for encryption.")

cron_expression = st.text_input("Please provide the cron expression for the file monitoring schedule.")

if st.button("Add Schedule", key="add_schedule_submit"):
    result = insert_file_watch_data(file_path, pgp_key_selected if pgp_or_not == "Yes" else None, cron_expression)
    print("Insertion result: ", result)
    if result == "insertion ok":
        st.success("Your expected file watch data has been saved!")
    else:
        st.error("An error occurred during insertion of file watch data: " + str(result))
