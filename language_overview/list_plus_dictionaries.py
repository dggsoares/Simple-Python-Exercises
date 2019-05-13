#!/usr/bin/env python3
# -*- coding: utf-8 -*-

targets = [
    {'ip': "54.145.216.193", 'real_location': 'Virginia', 'keyfile': 'key_USA.pem', 'services': ['HTTP', 'SQL Server']},
    {'ip': "18.222.205.211", 'real_location': 'Ohio', 'keyfile': 'key_USA_OHIO.pem', 'services': ['DHCP', 'GIT']},
    {'ip': "52.87.190.210", 'real_location': 'Virginia', 'keyfile': 'key_USA.pem', 'services': ['RPC', 'NTP']},
    {'ip': "35.176.16.183", 'real_location': 'London', 'keyfile': 'key_LONDON.pem', 'services': ['SMTP', 'DNS']},
    {'ip': "52.67.226.204", 'real_location': 'São Paulo', 'keyfile': 'key_BR.pem', 'services': ['HTTP', 'Netbios']},
    {'ip': "13.209.65.95", 'real_location': 'Seoul', 'keyfile': 'key_SEOUL.pem', 'services': ['SSH', 'SCP']},
    {'ip': "13.211.141.171", 'real_location': 'Syndey', 'keyfile': 'key_AUS.pem', 'services': ['FTP', 'HTTPS']}
]

for target in targets:
    print(f'''
        [+] IP: {target["ip"]}
            (-) Location: {target["real_location"]}
            (-) Pub Key File: {target["keyfile"]}
            (-) Services: {target["services"]}
        '''
    )