#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from pprint import pprint

with open('exercise21.txt', 'r') as file:
    for ip in file:
        ip = ip.replace('\n', '')
        url = f'http://{ip}/robots.txt'
        print(f'\n[+] ---- {ip} robots.txt content ---- [+]')
        try:
            r = requests.get(url, timeout=1)
            pprint(r.text)
        except requests.Timeout as e:
            print(f'\t[ERROR] {ip} TIMEOUT ERROR [ERROR]')
        print(f'[+] --------------------------------- [+]')
