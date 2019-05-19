#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = 'py.insidertips.xyz'
PORT = 30045


def do_math(a, b, operator):
    if operator == '+':
        return str(a + b).encode()
    elif operator == '-':
        return str(a - b).encode()
    elif operator == '*':
        return str(a * b).encode()
    elif operator == '/':
        return str(a / b).encode()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Banner
    print(s.recv(1024).decode())

    # First response
    # Raw data
    print('[+] First response')
    raw_data = s.recv(1024).decode()
    print(f'[+] Raw data: {raw_data}')

    # Split data
    split_data = raw_data.split('&')
    print(f'[+] Split data: {split_data}')

    a = int(split_data[0])
    b = int(split_data[1])
    operator = split_data[2]

    first_response = do_math(a, b, operator)
    s.send(first_response)
    print(f'[+] First reponse: {first_response}\n')

    # Second response
    # Raw data
    print('[+] Second response')
    raw_data = s.recv(1024).decode()
    print(f'[+] Raw data: {raw_data}')

    # Split data
    split_data = raw_data.split('&')
    print(f'[+] Split data: {split_data}')

    a = int(split_data[0])
    b = int(split_data[1])
    operator = split_data[2]

    second_response = do_math(a, b, operator)
    s.send(second_response)
    print(f'[+] Second reponse: {second_response}\n')

    # Third response
    # Raw data
    print('[+] Third response')
    raw_data = s.recv(1024).decode()
    print(f'[+] Raw data: {raw_data}')

    # Split data
    split_data = raw_data.split('&')
    print(f'[+] Split data: {split_data}')

    a = int(split_data[0])
    b = int(split_data[1])
    operator = split_data[2]

    third_response = do_math(a, b, operator)
    s.send(third_response)
    print(f'[+] Third response: {third_response}\n')

    # Correct message
    data = s.recv(1024).decode()
    print(data)
