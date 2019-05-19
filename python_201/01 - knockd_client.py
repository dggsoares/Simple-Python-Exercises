#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

host = '192.168.246.128'

ports = [
    {'number': 4433, 'protocol': 'tcp'},
    {'number': 8800, 'protocol': 'tcp'},
    {'number': 1234, 'protocol': 'udp'},
    {'number': 3088, 'protocol': 'tcp'},
]

challenge_port = 6667

for port in ports:
    if port['protocol'] == 'udp':
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto('something'.encode(), (host, port['number']))
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setblocking(False)
            s.connect_ex((host, port['number']))
            s.close()

print(f'Port {challenge_port} OPEN!')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, challenge_port))
    print(s.recv(3072).decode())

# Close port
ports = [7000, 8000, 9000]

for port in ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setblocking(False)
        s.connect_ex((host, port))
        s.close()

print(f'Port {challenge_port} CLOSED!')