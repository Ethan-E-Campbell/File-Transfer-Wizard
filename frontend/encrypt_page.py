import streamlit as st
from backend.encrypt import encrypt_file as ef
from backend.encrypt import list_imported_keys as lik
file_path = ""
pgp_public_key_file = ""

st.title("Welcome to the encrypt page.")
st.write("Please answer these questions to encrypt your file.")
#key_type = st.selectbox("What Key Type would you like to use for your PGP key pair?", lf(), index = 1)
imported_keys = lik()
#st.write(imported_keys)
#key_type = st.selectbox("What Key Type would you like to use for your PGP key pair?", imported_keys)
key_options = []
if key_options == []:
    for key in imported_keys:
        key_id = key['keyid']
        user = key['uids'][0]
        #st.write(key_id, user)
        key_options.append(f"{user} ({key_id})")
key_type = st.selectbox("What Key Type would you like to use for your PGP key pair?", key_options)
#key_type = st.selectbox("What Key Type would you like to use for your PGP key pair?", lf(), index = 1)


if st.button("Submit", key="file_encrypt_submit"):
    result = ef(file_path,file_bytes)
    st.write(result)

