import streamlit as st

home = st.Page("main_page.py", title="Home", icon="🎈")
encrypt_page = st.Page("encrypt.py", title="Encrypt a file", icon="🔐")
decrypt_page = st.Page("decrypt.py", title="Decrypt a file", icon="🔓")
send_page = st.Page("send.py", title="Send file", icon="📤")
create_keys_page = st.Page("create_keys.py", title="Create PGP key pair", icon="🗝️")

pg = st.navigation([
    home,
    encrypt_page,
    decrypt_page,
    send_page,
    create_keys_page
])

pg.run()
