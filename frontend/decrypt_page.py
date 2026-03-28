"""
Codeunit: decrypt_page.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Frontend page for decrypting PGP encrypted files.
"""

import streamlit as st
from backend.decrypt import decrypt_file as df

st.write("welcome to the decrypt page.")

#st.button("Decrypt a file", on_click=df())

footer = st.container() 
footer.divider() 
footer.caption("Ethan Campbell, 2026")