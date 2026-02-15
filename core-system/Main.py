import gnupg

def main_menu():
    print("Welcome to file tranfer wizard.\nThis wizard is meant to encrypt files using PGP encryption.\nPlease select an option!")
    main_menu = ("1. Encrypt a file" +
                 "\n2. Decrypt a file"+
                 "\n3. Create PGP key pair"+
                 "\n4. Create SSH key pair" +
                 "\n5. Exit\n")
    while True:
        try:
            internal_user_selection = int(input(main_menu))
            if internal_user_selection < 1 or internal_user_selection > 5:
                print("Invalid input. Please enter a number between 1 and 5.")
            else:
                return internal_user_selection
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def encrypt_file(file_path):
    pass

def decrypt_file(file_path):
    pass

def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG()
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)

if __name__ == "__main__":
    user_selection = None
    user_selection = main_menu()
    match user_selection:
        case 1: 
            print("You selected option 1, Encrypt File")
            pgp = create_gpg()
            file_obj = input("please enter the full file path of file to encrypt.")
        case 2: print("sweet")


