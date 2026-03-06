import gnupg
import uuid
import os
def create_uuid():
    return str(uuid.uuid4())
def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG(verbose = False, options = ['--verbose', '--batch', '--yes', '--pinentry-mode', 'loopback'])
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)


def create_pgp_key_pair(key_type, key_length, name_email, key_file_name):
    print ("Creating PGP key pair...")
    gpg = create_gpg()
    password = create_uuid()
    input_data= gpg.gen_key_input(key_type=key_type, key_length=key_length, passphrase=password)
    key = gpg.gen_key(input_data)
    print("Generated key: ", key)
    key_id = key.fingerprint
    KEYS_DIR = os.path.join(os.path.dirname(__file__), "..", "keys") 
    KEYS_DIR = os.path.abspath(KEYS_DIR)
    public_key_path = os.path.join(KEYS_DIR, (key_file_name + "_public_key.asc")) 
    private_key_path = os.path.join(KEYS_DIR, (key_file_name + "_private_key.asc"))
    ascii_armored_public_keys = gpg.export_keys(key_id, passphrase=password, output=public_key_path) # same as gpg.export_keys(keyids, False)
    ascii_armored_private_keys = gpg.export_keys(key_id, True, passphrase=password, output=private_key_path) # True => private keys
    print("Password: ", password)

    return key_id, password

def create_ssh_key_pair(file_path):
    print ("file encryption will happen here")