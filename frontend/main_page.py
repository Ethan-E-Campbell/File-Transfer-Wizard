import streamlit as st 


st.title("Welcome to File Transfer Wizard!") 
st.write("The file transfer wizard is a PGP encryption tool, with support for SFTP file transfers")
st.write("Please note! You must have GPG installed on your machine to use this tool.")
st.write("Please select a page from the sidebar to get started.")

footer = st.container() 
footer.divider() 
footer.caption("Ethan Campbell, 2026")