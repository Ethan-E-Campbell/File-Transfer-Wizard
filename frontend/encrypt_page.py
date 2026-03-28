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
    selection = st.selectbox("What key would you like to use for your PGP key pair?", list_keys_helper())
    #once submit is pressed, try to encrypt file.
    key_id = selection.split("(")[-1].strip(")")
    print("Key ID: ", key_id)
    if st.button("Submit", key="file_encrypt_submit"):
        result = ef(key_id)
        st.write(result)

    footer.caption("Ethan Campbell, 2026")

main()

