import streamlit as st 


st.title("Welcome to File Transfer Wizard!") 
st.write("The file transfer wizard is PGP encryption tool, with support for SFTP file transfer")
st.write("Please select a page from the sidebar to get started.")
st.write("If you wish to schedule a transfer, please use the schedule page to do so.")


footer = st.container() 
footer.divider() 
footer.caption("Ethan Campbell, 2026")