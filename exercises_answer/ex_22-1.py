#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import base64

def xor(message, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(message, key)])


URL = "http://localhost:3321"
key = 'PythonOffensive201#@113445'

r = requests.get(URL)
encoded_message = base64.b64decode(r.content)
decrypted_message = xor(encoded_message.decode(), key)
print(f'Received message : {r.content}')
print(f'Decrypted message : {decrypted_message}')
