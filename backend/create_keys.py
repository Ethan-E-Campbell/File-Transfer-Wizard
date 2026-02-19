import gnupg
import uuid
def create_uuid():
    return str(uuid.uuid4())
def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG(verbose = True, options = ['--verbose', '--batch', '--yes', '--pinentry-mode', 'loopback'])
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)


def create_pgp_key_pair(key_type, key_length, name_real, name_comment, name_email):
    print ("Creating PGP key pair...")
    gpg = create_gpg()
    password = create_uuid()
    input_data= gpg.gen_key_input(key_type="RSA", key_length=1024, passphrase=password)
    #input_data = gpg.gen_key_input(key_type=key_type, key_length=key_length, name_real=name_real, name_comment=name_comment, name_email=name_email)
    key = gpg.gen_key(input_data)
    print("Generated key: ", key)
    key_id = key.fingerprint
    ascii_armored_public_keys = gpg.export_keys(key_id, passphrase=password, output= 'C:\\Users\\Ethan\\Downloads\\public_key.asc') # same as gpg.export_keys(keyids, False)
    ascii_armored_private_keys = gpg.export_keys(key_id, True, passphrase=password, output= 'C:\\Users\\Ethan\\Downloads\\private_key.asc') # True => private keys
    print("Public Key: ", ascii_armored_public_keys)
    print("Private Key: ", ascii_armored_private_keys)
    print("Password: ", password)

    return key_id

def create_ssh_key_pair(file_path):
    print ("file encryption will happen here")