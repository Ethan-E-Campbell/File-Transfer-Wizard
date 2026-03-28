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


def encrypt_file(key_id, file):
    try:
        print ("Starting file encryption process....")
        #print("public Key ", public_key_path)
        gpg = create_gpg()

        #import_result = gpg.import_keys(public_key_path)
        #print("Import Result: ", import_result.fingerprints)
        #if not import_result.fingerprints: 
        #    raise ValueError("No valid public keys were imported")
        output = "C:\\Users\\Ethan\\Downloads\\output.gpg"
        result = gpg.encrypt(file, recipients=key_id,  output=output)
    except Exception as e:
        print("An error occurred during file encryption: ", e)
        return e
    return result.status

def key_options_default():
    gpg = create_gpg()
    keys = gpg.list_keys()
    key_options = []
    if key_options == []:
        for key in keys:
            print("Key: ", key)
            key_id = key['keyid']
            user = key['uids'][0]
            key_options.append(f"{user} ({key_id})")
    return key_options