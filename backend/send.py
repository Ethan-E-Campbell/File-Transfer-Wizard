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
        transport.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        transport.connect(hostname=hostname, port=port,
                          username=username, password=password)
        return transport.open_sftp()
    except Exception as e:
        print("An error occurred while connecting to the SFTP server: ", e)
        return


def send_file(file_name, file_path, hostname):
    print("send file will happen here")
    sftp = sftp_client_setup('127.0.0.1', 22, "ec",
                             "ec")
    if sftp:
        try:
            print("Sending file...")
            print(f"File name: {file_name}")
            print(f"File path: {file_path}")
            #sftp.mkdir('/upload')
            sftp.put(file_name, '/upload/wakanda.jpg')
            print("File sent successfully!")
        except Exception as e:
            print("An error occurred while sending the file: ", e)
        finally:
            sftp.close()
