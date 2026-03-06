import streamlit as st
from backend.create_keys import create_pgp_key_pair as cpgpkp
from backend.create_keys import create_ssh_key_pair as csshkp



st.write("welcome to the key creation page.")
pgp_or_ssh = st.selectbox("Are you creating a PGP or SSH key pair?", ["PGP", "SSH"])

if pgp_or_ssh == "PGP":
    #input_data = gpg.gen_key_input(key_type=key_type, key_length=key_length, name_real=name_real, name_comment=name_comment, name_email=name_email)
    st.write("You have selected to create a PGP key pair.")
    key_type = st.selectbox("What Key Type would you like to use for your PGP key pair?", ["RSA", "DSA"], index = 0)
    key_length = st.selectbox("What Key Length would you like to use for your PGP key pair?", [1024, 2048, 4096], index = 1)
    name_email = st.text_input("What Name-Email would you like to use for your PGP key pair?")
    key_file_name = st.text_input("What would you like to name your key files? (without extension)")
    if st.button("Submit", key="pgp_key_submit"):
        if not key_file_name.strip(): 
            st.error("Please enter a name for your key files before submitting.")
        else: 
            fingerprint, password = cpgpkp(key_type, key_length, name_email, key_file_name)
            st.write("Fingerprint: ", fingerprint)
            st.write("Password: ", password)