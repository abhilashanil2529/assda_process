# #!/usr/bin/env python
#
# """
# An RFC-4217 asynchronous FTPS server supporting both SSL and TLS.
# Requires PyOpenSSL module (http://pypi.python.org/pypi/pyOpenSSL).
# """
# import ftplib
#
# remote_conn = ftplib.FTP()
# remote_conn.connect('3.18.20.149', 7368)
# remote_conn.login('anilmathew', '0TWRLb9lbfi3jP5h5U986J')
# remote_conn.nlst()
# print(">>>>>>>>>>>>>>>>>>>>>>")
# from pyftpdlib.servers import FTPServer
# from pyftpdlib.authorizers import DummyAuthorizer
# import os
# from pyftpdlib.servers import FTPServer
# from pyftpdlib.handlers import FTPHandler
#
# def main():
#     authorizer = DummyAuthorizer()
#     authorizer.add_user('anilmathew', '0TWRLb9lbfi3jP5h5U986J', os.getcwd(), perm='elradfmw')
#     authorizer.add_anonymous('.')
#     handler = FTPHandler
#     handler.authorizer = authorizer
#     handler.masquerade_address = '3.18.20.149'
#     # requires SSL for both control and data channel
#     handler.tls_control_required = True
#     handler.tls_data_required = True
#     handler.passive_ports = range(60000, 60099)
#     server = FTPServer(('', 7368), handler)
#     server.serve_forever()
#
#
#
#
# if __name__ == '__main__':
#     main()
#
#
# from paramiko import SSHClient
# from paramiko import AutoAddPolicy
#
# from asplinks import settings
#
# ssh = SSHClient()
# ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(AutoAddPolicy())
# ssh.connect("sftp.accelya.com", username="CA031", password="289SEP20")
# import stat
#
# ftp = ssh.open_sftp()
# print("SSSSSSSSSSSSSSSSSSSSSSSSS",ftp)
# print("ftp.listdir_attr():",ftp.listdir_attr())
#
# for fileattr in ftp.listdir_attr():
#     print(fileattr.st_mode,">>>>>>>>>",fileattr.filename)
#     if not stat.S_ISDIR(fileattr.st_mode):
#         filename = fileattr.filename

