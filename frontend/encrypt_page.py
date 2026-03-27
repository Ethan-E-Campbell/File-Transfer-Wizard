import streamlit as st
from backend.encrypt import encrypt_file as ef
from backend.encrypt import key_options_default as kod


@st.cache_data
def list_keys_helper():
    return kod()


def main():
    # Main print statements
    st.title("Welcome to the encrypt page.")
    st.write("Please answer these questions to encrypt your file.")
    #ask what key to use
    key_type = st.selectbox("What key would you like to use for your PGP key pair?", list_keys_helper())
    #once submit is pressed, try to encrypt file.

    if st.button("Submit", key="file_encrypt_submit"):
        result = ef(file_path,file_bytes)
        st.write(result)

main()

