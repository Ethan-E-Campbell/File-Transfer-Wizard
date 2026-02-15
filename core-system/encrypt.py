import gnupg
def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG()
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)


def encrypt_file(file_path):
    print ("file encryption will happen here")