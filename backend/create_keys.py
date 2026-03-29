"""
Codeunit: create_keys.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Creates PGP and SSH key pairs for encryption.
"""

import gnupg
import uuid
import os
import keyring
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

def store_passphrase(fingerprint, passphrase):
    keyring.set_password("gpg-passphrases", fingerprint, passphrase)

def create_pgp_key_pair(key_type, key_length, name_email, name_real):
    print ("Creating PGP key pair...")
    gpg = create_gpg()
    password = create_uuid()
    input_data= gpg.gen_key_input(key_type=key_type, key_length=key_length, passphrase=password, name_email=name_email, name_real = name_real)
    key = gpg.gen_key(input_data)
    store_passphrase(key.fingerprint, password)
    #print("Generated key: ", key)
    #print("Password: ", password)
    return key.fingerprint, password

def create_ssh_key_pair(file_path):
    print ("file encryption will happen here")