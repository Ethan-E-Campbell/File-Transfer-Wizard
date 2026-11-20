"""
Codeunit: file_watch_report.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Query SQLite database to deliver a report of configured
             file watchers.
"""

import pandas as pd
import streamlit as st
from backend.filewatch_db import retrieve_file_watch_data


file_watch_data = retrieve_file_watch_data()
file_watch_dataframe = pd.DataFrame(
    file_watch_data,
    columns=["unique_id", "file_watch_path", "pgp_key", "cron_expression"],
)

st.dataframe(file_watch_dataframe, width="stretch", hide_index=True)

footer = st.container()
footer.divider()
footer.caption("Ethan Campbell, 2026")
