import streamlit as st
from backend.encrypt import encrypt_file as ef
from backend.encrypt import key_options_default as key_options_default
file_path = ""
pgp_public_key_file = ""

@st.cache_data
def list_keys_helper():
    return key_options_default()

def title():
    st.title("Welcome to the encrypt page.")
    st.write("Please answer these questions to encrypt your file.")
    return None

def submit(): 
    if st.button("Submit", key="file_encrypt_submit"):
        result = ef(file_path,file_bytes)
        st.write(result)
def options():
    key_type = st.selectbox("What key would you like to use for your PGP key pair?", list_keys_helper())
def submit(): 
    if st.button("Submit", key="file_encrypt_submit"):
        result = ef(file_path,file_bytes)
        st.write(result)

title()
options()
submit()

