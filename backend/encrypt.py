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
    try:
        print ("Starting file encryption process....")
        gpg = create_gpg()

        import_result = gpg.import_keys_file(public_key_path)
        print("Import Result: ", import_result.fingerprints)
        if not import_result.fingerprints: raise ValueError("No valid public keys were imported")
        result = gpg.encrypt_file(open(file_path, 'rb'), recipients=import_result.fingerprints,  output=file_path + '.gpg')
    except Exception as e:
        print("An error occurred during file encryption: ", e)
        return e
    return result.status