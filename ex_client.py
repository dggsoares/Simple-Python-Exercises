#!/usr/bin/env python3

import socket

HOST = 'localhost'
PORT = 30001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(4096).decode())
    s.sendall('Hello Word from Python Sockets!'.encode())
    data = s.recv(4096)

print(f'{data.decode()}')
