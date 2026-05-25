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



file_name = st.text_input("What file do you wish to send?")
file_path = st.text_input("What is the file path of the file you wish to send?")
hostname = st.text_input("What is the hostname of the SFTP server you wish to send to?")

if st.button("Submit", key="file_send_submit"):
    send_file(file_name,file_path, hostname)
    st.write("Your file has been sent successfully!")
