"""
Codeunit: decrypt.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Decrypts PGP encryptted files.
"""
import keyring

import keyring
import gnupg
def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG(verbose = True, options = ['--verbose', '--batch', '--yes', '--pinentry-mode', 'loopback'])
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)

def load_passphrase(fingerprint):
    return keyring.get_password("gpg-passphrases", fingerprint)

def decrypt_file(file_data, fingerprint):

    print ("file decryption will happen here")
    gpg = create_gpg()
    print(fingerprint)
    passphrase = load_passphrase(fingerprint)
    print("Loaded passphrase: ", passphrase)
    decrypted_data = gpg.decrypt(file_data, passphrase=passphrase)
    print("Decryption status: ", decrypted_data.status)
    print("Decrypted data: ", decrypted_data.data)

def key_options_default():
    gpg = create_gpg()
    keys = gpg.list_keys()
    key_options = []
    if key_options == []:
        for key in keys:
            key_id = key['fingerprint']
            user = key['uids'][0]
            key_options.append(f"{user} ({key_id})")
    return key_options