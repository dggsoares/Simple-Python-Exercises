#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Python dictionaries')

dict0 = {}

dict1 = dict(a=1, b=-2, c=3, d=4, e=5)

dict2 = dict(
    one=1,
    two=2,
    three=3,
    four=4,
    five=5
)

dict3 = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}

dict4 = {'name': 'Bob', 'last_name': 'Williams', 'age': 16}

print(dict0)
print(dict1)
print(dict2)
print(dict3)
print(f'Customer name: {dict4["name"]}, Last Name: {dict4["last_name"]} Age: {dict4["age"]}')
print('name' in dict4)
print('Bob' in dict4.values())
print(dict4.values())
print(dict4.items())