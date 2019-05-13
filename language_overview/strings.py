#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Strings
print('------------ Building Strings ------------')

string1 = 'This is a string. We built in single quotes'
string2 = "This is also a string. We built in double quotes"

string3 = '''
    This is built using triple quotes, 
    so it can span 
    multiple lines
'''

string4 = """
    This is built using triple double-quotes, 
    so it can span 
    multiple lines too.
"""

print(string1)
print(string2)
print(string3)
print(string4)

print('--------------------------------------------')

print()

# Formatting Strings

print('------------ Formatting strings ------------')

name = 'John'
last_name = 'Williams'

print('Hi, %s!' % name)
print('Hi {} {}!'.format(name, last_name))
print('Hi {1} {0}!'.format(last_name, name))
print('Hi {1} {0}!'.format(name, last_name))
print('Hi {name} {last_name}!'.format(name=name, last_name=last_name))
print(f'Hi {name} {last_name}!!')

print('--------------------------------------------')

print()

# String slicing
# str[start:end]

print('-------------- String slicing --------------')

str1 = 'String slicing'
str2 = "Special cases aren't special enough to break the rules."

print(f'List from str1: {list(str1)}')
print(f'Character in "str2" at position 0: {str2[0]}')
print(f'Character at "str2" position 0: {str2[3]}')
print(f'str2[:10]: {str2[:10]}')
print(f'str2[8:]: {str2[8:]}')
print(f'Extract "cases" word (positive index): {str2[8:13]}')
print(f'Extract "break" word (negative index): {str2[-16:-11]}')

for index, character in enumerate(str2):
    print(f'{index} : {character}')

print(list(enumerate(str1)))