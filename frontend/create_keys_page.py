import streamlit as st
from backend.create_keys import create_pgp_key_pair as cpgpkp
from backend.create_keys import create_ssh_key_pair as csshkp



st.write("welcome to the key creation page.")
pgp_or_ssh = st.text_input("Are you creating a PGP or SSH key pair?")





pgp_public_key = st.text_input("please enter the full file path of the public key you want to encrypt with: ")
#if st.button("Submit", key="file_encrypt_submit"):
#    result = ef(file_path,pgp_public_key)
#    #st.write(e)
#    st.write(result)

#if st.button("Encrypt a file", key="file_encrypt_show") and enable_inputs == False:
#    enable_inputs = True
#    show_encrypt_inputs()