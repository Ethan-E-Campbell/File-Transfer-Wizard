"""
Codeunit: send.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Dends files using SFTP.
"""
import paramiko


def sftp_client_setup(hostname, port, username, password):
    try:
        print("Setting up SFTP client...")
        transport = paramiko.client.SSHClient()
        # This should be fixed later...to ask if the user trusts the key. 
        # Or to use some kind of host key management system.
        transport.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        transport.connect(hostname=hostname, port=port,
                          username=username, password=password)
        return transport.open_sftp()
    except Exception as e:
        print("An error occurred while connecting to the SFTP server: ", e)
        return e


def send_file(file_name_and_path, file_send_path, hostname,
              port, username, password):
    try:
        sftp = sftp_client_setup(hostname, port, username, password)
        if isinstance(sftp, Exception):
            return sftp

        # print("Sending file...")
        # print(f"File name: {file_name_and_path}")
        # print(f"File path: {file_send_path}")
        # sftp.mkdir('/upload')
        sftp.put(file_name_and_path, file_send_path)
        print("File sent successfully!")
        sftp.close()
        return None
    except Exception as e:
        print("An error occurred while sending the file: ", e)
        return e
