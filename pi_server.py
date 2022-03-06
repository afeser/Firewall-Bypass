"""
raspberry pi uzerindeki server bu!

buradaki olay, gelen veriyi local ssh portuna yonlendiriyor
"""
from common import encrypt, decrypt
import socket
import numpy as np

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
print('Listening on', PORT)

BLOCKED_PORT = 10022

# socket connecting to the ssh server
ssh_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssh_server_socket.connect(('localhost', BLOCKED_PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()


def listen_to_remote_send_to_local_ssh():
    while True:
        data = conn.recv(1024)
        print('Data read from remote with length', len(data))
        data = decrypt(data)

        ssh_server_socket.sendall(data)
        if not data:
            break

        
def listen_to_local_ssh_send_to_remote():
    while True:
        data = ssh_server_socket.recv(1024)
        print('Data read from local SSH with length', len(data))
        # encrypt data
        data = encrypt(data)

        conn.sendall(data)
        if not data:
            break

import threading
t1 = threading.Thread(target=listen_to_remote_send_to_local_ssh)
t2 = threading.Thread(target=listen_to_local_ssh_send_to_remote)

t1.start()
t2.start()

t1.join()
t2.join()

print('Program terminated successfully')
