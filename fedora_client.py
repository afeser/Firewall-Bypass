"""
this is the client where it sends requests to the server

run this on the local server and connect to the remote blocked port
"""
from common import encrypt, decrypt, partial_send
import socket
import numpy as np

REMOTE_IP = 'localhost'

# THE DUAL OF THIS PROGRAM!
REMOTE_DUAL_PORT = 8080

# WHERE WE SHOULD SSH INTO?
LOCAL_PORT = 8001

# socket connecting to the ssh server
remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remote_socket.connect((REMOTE_IP, REMOTE_DUAL_PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', LOCAL_PORT))
s.listen()
conn, addr = s.accept()

tag1 = '<html>'.encode('utf-8')
def listen_to_local_send_to_remote():
    while True:
        data = conn.recv(1024)
        print('Data read from local with length', len(data))
        # encrypt here
        data = encrypt(data)

        remote_socket.sendall(data)
        if not data:
            break

        
def listen_to_remote_send_to_local():
    while True:
        data = remote_socket.recv(1024)
        print('Data read from remote with length', len(data))
        # decrypt
        data = decrypt(data)

        conn.sendall(data)
        if not data:
            break

import threading
t1 = threading.Thread(target=listen_to_local_send_to_remote)
t2 = threading.Thread(target=listen_to_remote_send_to_local)

t1.start()
t2.start()

t1.join()
t2.join()

print('Program terminated successfully')
