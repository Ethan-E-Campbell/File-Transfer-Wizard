import streamlit as st
from backend.encrypt import encrypt_file as ef
from backend.encrypt import list_files as lf
enable_inputs = False
file_path = ""
pgp_public_key_file = ""

st.title("Welcome to the encrypt page.")
st.write("Please answer these questions to encrypt your file.")
st.write(lf())
file_path = st.text_input("Enter the path to the file you want to encrypt:")
pgp_public_key_file = st.file_uploader("please upload the public key you want to encrypt with:") 

if pgp_public_key_file: 
    st.write("You selected:", pgp_public_key_file.name)
    pgp_public_key_data = pgp_public_key_file.read()

if st.button("Submit", key="file_encrypt_submit"):
    result = ef(file_path,file_bytes)
    st.write(result)

