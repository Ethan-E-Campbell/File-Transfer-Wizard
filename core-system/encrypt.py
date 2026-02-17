import gnupg
import os
def create_gpg():
    try:
        print("Initializing GPG...")
        gpg_path = r"C:\Program Files\GnuPG\bin"  # Update this path if necessary
        os.environ["PATH"] += os.pathsep + gpg_path
        gpg = gnupg.GPG()
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)


def encrypt_file(file_path):
    print ("Starting file encryption process....")
    gpg = create_gpg()
    key = gpg.gen_key()
    print("Generated key: ", key)