import gnupg
import os
def create_gpg():
    try:
        print("Initializing GPG...")
        gpg = gnupg.GPG(verbose = True, options = ['--verbose', '--batch', '--yes', '--pinentry-mode', 'loopback'])
        return gpg
    except Exception as e:
        print("An error occurred while initializing GPG: ", e)
        exit(1)


def encrypt_file(file_path, public_key_path):
    print ("Starting file encryption process....")
    gpg = create_gpg()

    import_result = gpg.import_keys_file(public_key_path)
    print("Import Result: ", import_result.fingerprints)
    gpg.encrypt_file(open(file_path, 'rb'), recipients=import_result.fingerprints,  output=file_path + '.gpg')