import streamlit as st
from backend.encrypt import encrypt_file as ef

def run_encrypt(): 
    ef('', '')


st.write("welcome to the encrypt page.")


st.button("Encrypt a file", on_click= run_encrypt)