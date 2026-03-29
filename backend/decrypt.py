"""
Codeunit: decrypt.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Decrypts PGP encryptted files.
"""
import os
import keyring
import gnupg


def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG(verbose=False, options=['--verbose',
                                                '--batch', '--yes',
                                                '--pinentry-mode', 'loopback'])
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)


def load_passphrase(fingerprint):
    return keyring.get_password("gpg-passphrases", fingerprint)


def decrypt_file(file_data,
                 fingerprint,
                 output_file_name_with_ext,
                 output_path=None):

    gpg = create_gpg()

    if output_path is None or output_path == "":
        output_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                   "..", "output"))
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    full_file_path = os.path.join(output_path, output_file_name_with_ext)
    passphrase = load_passphrase(fingerprint)
    decrypted_data = gpg.decrypt(file_data,
                                 passphrase=passphrase,
                                 output=full_file_path)

    return decrypted_data.status, full_file_path


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
