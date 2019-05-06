#!/usr/bin/env python3

import socket

HOST = '178.128.157.183'
PORT = 30030

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(4096).decode())
    s.sendall('Hello Word!'.encode())
    data = s.recv(4096)

print(f'{data.decode()}')
