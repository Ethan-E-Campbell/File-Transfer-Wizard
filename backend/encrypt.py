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


def encrypt_file(file_path, public_key_path):
    try:
        print ("Starting file encryption process....")
        print("public Key ", public_key_path)
        gpg = create_gpg()

        import_result = gpg.import_keys(public_key_path)
        print("Import Result: ", import_result.fingerprints)
        if not import_result.fingerprints: 
            raise ValueError("No valid public keys were imported")
        result = gpg.encrypt_file(open(file_path, 'rb'), recipients=import_result.fingerprints,  output=file_path + '.gpg')
    except Exception as e:
        print("An error occurred during file encryption: ", e)
        return e
    return result.status

def key_options_default():
    imported_keys = list_imported_keys()
    key_options = []
    if key_options == []:
        for key in imported_keys:
            key_id = key['keyid']
            user = key['uids'][0]
            #st.write(key_id, user)
            key_options.append(f"{user} ({key_id})")
    return key_options

def list_imported_keys():
    gpg = create_gpg()
    keys = gpg.list_keys() 
    return keys