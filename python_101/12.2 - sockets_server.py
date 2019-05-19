#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = '127.0.0.1'
PORT = 45001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(f'Server listening on port: {PORT}...')
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    conn.sendall('Hello Human!'.encode())