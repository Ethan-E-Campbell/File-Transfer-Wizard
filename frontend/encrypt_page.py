import streamlit as st
from backend.encrypt import encrypt_file as ef
enable_inputs = False
file_path = ""
pgp_public_key = ""

st.write("welcome to the encrypt page.")
st.write("Please answer these questions to encrypt your file.")
file_path = st.text_input("Enter the path to the file you want to encrypt:")
pgp_public_key = st.text_input("please enter the full file path of the public key you want to encrypt with: ")
if st.button("Submit", key="file_encrypt_submit"):
    result = ef(file_path,pgp_public_key)
    #st.write(e)
    st.write(result)

#if st.button("Encrypt a file", key="file_encrypt_show") and enable_inputs == False:
#    enable_inputs = True
#    show_encrypt_inputs()