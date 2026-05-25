"""
Codeunit: send_page.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Frontend page for sending files using SFTP.
"""

import streamlit as st
from backend.send import send_file as send_file
st.write("SFTP send feature enhancement coming soon")

footer = st.container()
footer.divider()
footer.caption("Ethan Campbell, 2026")
send_file("file_path", "hostname")
