#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import base64

HOST = 'localhost'
PORT = 30030

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Banner
    print(s.recv(1024).decode())

    # Encoded data
    encoded_data = s.recv(1024)
    print(f'[+] Encoded data : {encoded_data}')

    # Decoded data
    decode_data = base64.b64decode(encoded_data)
    print(f'[+] Decoded data : {decode_data}')

    # Send first 10 characters from decoded data
    slice_decoded_data = decode_data[:10]
    s.send(slice_decoded_data)
    print(f'[+] Slice decoded data : {slice_decoded_data}\n')

    # Receive response
    data = s.recv(1024).decode()
    print(data)