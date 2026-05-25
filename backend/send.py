"""
Codeunit: send.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Dends files using SFTP.
"""
import paramiko


def sftp_client_setup(hostname, port, username, password, file_path, remote_path):
    try:
        print("Setting up SFTP client...")
        transport = paramiko.client.SSHClient()
        transport.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        transport.connect(hostname=hostname, port=port,
                          username=username, password=password)

def send_file(file_path, hostname):
    print("send file will happen here")
    sftp_client_setup(hostname, 22, "username", "password", file_path, "remote_path")
