#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import base64

HOST = 'py.insidertips.xyz'
PORT = 30001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Banner
    print(s.recv(2048).decode())

    # Response
    message = 'Hello World!'.encode()
    s.send(message)
    print(f'Message sent: {message}\n')

    # Receive response
    data = s.recv(1024).decode()
    print(data)