#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = 'towel.blinkenlights.nl'
PORT = 23

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print(s.recv(1024).decode(), end='')

