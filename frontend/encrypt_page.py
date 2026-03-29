"""
Codeunit: encrypt_page.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Frontend page for file encryption.
"""

import streamlit as st
from backend.encrypt import encrypt_file as encrypt_file
from backend.encrypt import key_options_default as key_options


@st.cache_data
def list_keys_helper():
    return key_options()


def main():
    # Variable declaration
    upload_or_path = None
    file_path = None
    uploaded_file = None
    bytes_data = None
    file_name = None
    # Main print statements
    st.title("Welcome to the encrypt page.")
    st.write("Please answer these questions to encrypt your file.")
    # ask what key to use
    selection = st.selectbox("What key would you like to use for decryption?", list_keys_helper())
    key_id = selection.split("(")[-1].strip(")")
    # print("Key ID: ", key_id)
    # ask for file path or uploaded file

    upload_or_path = st.selectbox("Please upload a file or enter a file path", [ "Upload a file", "Enter a file path"])
    if upload_or_path == "Enter a file path":
        file_path = st.text_input("Please enter the file path of the file you would like to encrypt.") 
    elif upload_or_path == "Upload a file":
        uploaded_file = st.file_uploader("Choose a file to upload")
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            file_name = uploaded_file.name

    output_file_name_with_ext = st.text_input("Please give a name for your encrypted file. Include extention (.ext) if expected output is not .PGP")
    output_path = st.text_input("Please enter file path where you wannt encrypted file. If left blank, the file will be saved in an output folder.")

    if st.button("Submit", key="file_encrypt_submit"):
        if upload_or_path is None or upload_or_path == "" or (bytes_data is None and file_path is None):
            st.error("Please select a file input method before submitting.")
            return
        result, output_file_path = encrypt_file(key_id, file_path if upload_or_path == "Enter a file path" else bytes_data, file_name, output_file_name_with_ext, output_path)
        if result == "encryption ok":
            st.success("Your file has been encrypted successfully! Here is the full file path:" + output_file_path )
        else:
            st.error("An error occurred during encryption: " + str(result))

    footer = st.container()
    footer.divider()
    footer.caption("Ethan Campbell, 2026")


main()
