"""
Codeunit: file_watch_report.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Query Sqlite database to deliver report on currently set up filewatchers.
"""

import streamlit as st
from backend.filewatch_db import retrieve_file_watch_data as retrieve_file_watch_data


print(retrieve_file_watch_data())

footer = st.container()
footer.divider()
footer.caption("Ethan Campbell, 2026")
