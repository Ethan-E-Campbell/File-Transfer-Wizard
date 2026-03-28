import streamlit as st
from backend.encrypt import encrypt_file as encrypt_file
from backend.encrypt import key_options_default as key_options


@st.cache_data
def list_keys_helper():
    return key_options()


def main():
    # Main print statements
    st.title("Welcome to the encrypt page.")
    st.write("Please answer these questions to encrypt your file.")
    #ask what key to use
    selection = st.selectbox("What key would you like to use for your PGP key pair?", list_keys_helper())
    key_id = selection.split("(")[-1].strip(")")
    print("Key ID: ", key_id)
    #ask for file path or uploaded file
    upload_or_path = st.selectbox("Would you like to upload a file or enter a file path?", ["Upload a file", "Enter a file path"])
    if upload_or_path == "Enter a file path":
        file_path = st.text_input("Please enter the file path of the file you would like to encrypt.") 
    elif upload_or_path == "Upload a file":
        uploaded_file = st.file_uploader("Choose a file to upload")
    else:
        st.error("Please select a valid option for file input.")
    #once submit is pressed, try to encrypt file.
    print("uploaded file: ", uploaded_file)
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    if st.button("Submit", key="file_encrypt_submit"):
        result = encrypt_file(key_id, file_path if upload_or_path == "Enter a file path" else bytes_data)
        st.write(result)

    footer = st.container() 
    footer.divider() 
    footer.caption("Ethan Campbell, 2026")

main()

