"""
Codeunit: encrypt.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Encrypts file using PGP.
"""

import gnupg
import os
def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG(verbose = False, options = ['--verbose', '--batch', '--yes', '--pinentry-mode', 'loopback'])
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)


def encrypt_file(key_id, file_byte_data, file_name, output_file_name_with_ext, output_path = None):
    try:
        print ("Starting file encryption process....")
        gpg = create_gpg()
        if output_file_name_with_ext[-3:] != ".pgp" and output_file_name_with_ext.find(".") == -1:
            output_file_name_with_ext += ".pgp"
        if output_path is None or output_path == "":
            output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            
        full_file_path = os.path.join(output_path, output_file_name_with_ext)
        result = gpg.encrypt(file_byte_data, recipients=key_id,  output=full_file_path)
    except Exception as e:
        print("An error occurred during file encryption: ", e)
        return e
    return result.status, output_path

def key_options_default():
    gpg = create_gpg()
    keys = gpg.list_keys()
    key_options = []
    if key_options == []:
        for key in keys:
            key_id = key['keyid']
            user = key['uids'][0]
            key_options.append(f"{user} ({key_id})")
    return key_options