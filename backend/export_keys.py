"""
Codeunit: export_keys.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Allows the exporting of keys to to files. Use with care.
"""

# KEYS_DIR = os.path.join(os.path.dirname(__file__), "..", "keys") 
# KEYS_DIR = os.path.abspath(KEYS_DIR)
# public_key_path = os.path.join(KEYS_DIR, (key_file_name + "_public_key.asc")) 
# private_key_path = os.path.join(KEYS_DIR, (key_file_name + "_private_key.asc"))
# ascii_armored_public_keys = gpg.export_keys(key_id, passphrase=password, output=public_key_path) # same as gpg.export_keys(keyids, False)
# ascii_armored_private_keys = gpg.export_keys(key_id, True, passphrase=password, output=private_key_path) # True => private keys