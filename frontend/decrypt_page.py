"""
Codeunit: decrypt_page.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Frontend page for decrypting PGP encrypted files.
"""

import streamlit as st
from backend.decrypt import decrypt_file as decrypt_file
from backend.encrypt import key_options_default as key_options

@st.cache_data
def list_keys_helper():
    return key_options()

st.title("Welcome to the decrypt page.")

upload_or_path = st.selectbox("Please upload a file or enter a file path", [ "Upload a file", "Enter a file path"])
if upload_or_path == "Enter a file path":
    file_path = st.text_input("Please enter the file path of the file you would like to encrypt.") 
elif upload_or_path == "Upload a file":
    uploaded_file = st.file_uploader("Choose a file to upload")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        file_name = uploaded_file.name

selection = st.selectbox("What key would you like to use for decryption?", list_keys_helper())
key_id = selection.split("(")[-1].strip(")")
if st.button("Decrypt a file", key="file_encrypt_submit"):
    decrypt_file(file_path if upload_or_path == "Enter a file path" else bytes_data)

footer = st.container() 
footer.divider() 
footer.caption("Ethan Campbell, 2026")