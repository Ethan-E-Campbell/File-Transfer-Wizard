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

file_name_and_path = st.text_input("Input full file path of the file you wish to send.")
file_send_path = st.text_input("Input the full file path you wish to send the file to on the SFTP server. ")
hostname = st.text_input("What is the hostname of the SFTP server " +
                         "you wish to send to?")
port = st.text_input("What is the port number of the SFTP server " +
                      "you wish to send to? (default is 22)")

if st.button("Submit", key="file_send_submit"):
    send_file(file_name_and_path, file_send_path, hostname, port)
    st.write("Your file has been sent successfully!")
