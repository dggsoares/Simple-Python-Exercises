#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ipwhois import IPWhois
import json
import pickle

# Ex 1.1
# Read a file called 'exercise11.txt' with IPs, create a list of targets using the data structures Lists
# and Dictionaries and print them.

from pprint import pprint

targets = []

with open('exercise11.txt', 'r') as file:
    for ip in file:
        aux = {'ip': ip.replace('\n', '')}
        targets.append(aux)

# pprint(targets)

# Ex 1.2
# Using the Whois library see information for each target present in the list created in the previous exercise
# and update the information for each IP in the list.

for index, target in enumerate(targets):
    # Whois Lookup
    print(f'{index} : {target["ip"]}')

    lookup = IPWhois(target['ip']).lookup_whois()
    cidrs = [cidr for line in lookup['nets'] for cidr in line['cidr'].replace(' ', '').split(',')]
    description = [line['description'].replace('\n', '') for line in lookup['nets'] if line['description'] is not None]
    address = [line['address'].replace('\n', '') for line in lookup['nets'] if line['address'] is not None]
    emails = [email for line in lookup['nets'] if line['emails'] if not None for email in line['emails']]

    # Information retrivied
    target['cidrs'] = cidrs
    target['descriptions'] = description
    target['address'] = address
    target['emails'] = emails

    # Update the target list
    targets[index] = target

# Ex 1.3
# Write in file called 'exercise13.txt' the lists of targets used in the previous exercise.

with open('execises13.txt', 'w') as file_output:
    for target in targets:
        file_output.write(str(target))
        file_output.write('\n')

with open('execises13_json.txt', 'w') as file_output_json:
    file_output_json.write(json.dumps(targets))

with open('execises13_pickle.txt', 'wb') as file_output_pickle:
    file_output_pickle.write(pickle.dumps(targets))

# Reading targets list from file

with open('execises13.txt', 'r') as file_input:
    print('\n----- STANDARD LOADS -----')
    # for line in file_input:
    #     targets.append(dict(line))

with open('execises13_json.txt', 'r') as file_input_json:
    targets = json.loads(file_input_json.read())

    print('\n----- JSON LOADS -----')
    pprint(targets)
    print('\n----- HOST INFORMATION -----')
    print(f'IP: {targets[3]["ip"]}')
    print(f'Descriptions: {targets[3]["descriptions"]}')
    print(f'CIDRs: {targets[3]["cidrs"]}')
    print(f'Adress: {targets[3]["address"]}')
    print('---------------------------')

with open('execises13_pickle.txt', 'rb') as file_input_pickle:
    targets = pickle.loads(file_input_pickle.read())

    print('\n----- PICKLE LOADS -----')
    pprint(targets)

