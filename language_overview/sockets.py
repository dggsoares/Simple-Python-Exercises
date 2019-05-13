#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = '127.0.0.1'
PORT = 45001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024).decode()

print(data)