from encrypt import encrypt_file
from decrypt import decrypt_file
from send import send_file
from create_keys import create_pgp_key_pair, create_ssh_key_pair

def main_menu():
    print("Welcome to file tranfer wizard.\nThis wizard is meant to encrypt files using PGP encryption.\nPlease select an option!")
    main_menu = ("1. Encrypt a file" +
                 "\n2. Decrypt a file"+
                 "\n3. Create PGP key pair"+
                 "\n4. Create SSH key pair" +
                 "\n5. Send file" +
                 "\n6. Exit\n")
    while True:
        try:
            internal_user_selection = int(input(main_menu))
            if internal_user_selection < 1 or internal_user_selection > 5:
                print("Invalid input. Please enter a number between 1 and 5.")
            else:
                return internal_user_selection
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    user_selection = None
    user_selection = main_menu()
    match user_selection:
        case 1: 
            print("You selected option 1, Encrypt File")
            #pgp = create_gpg()
            file_obj = input("please enter the full file path of file to encrypt: ")
            encrypt_file(file_obj)
        case 2: 
            print("You selected option 2, Decrypt File")
            file_obj = input("please enter the full file path of file to decrypt.")
            decrypt_file(file_obj)
        case 3: 
            print("You selected option 3, Create PGP Key Pair")
            create_pgp_key_pair()
        case 4: 
            print("You selected option 4, Create SSH Key Pair")
            create_ssh_key_pair()
        case 5: 
            print("You have selected option 5, Send File")
            file_obj = input("please enter the full file path of file to send.")
        case 6: 
            print("Exiting program. Goodbye!")


