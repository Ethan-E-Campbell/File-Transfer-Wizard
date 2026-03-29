"""
Codeunit: send.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Dends files using SFTP.
"""

import gnupg
def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG()
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)


def send_file(file_path):
    print ("send file will happen here")