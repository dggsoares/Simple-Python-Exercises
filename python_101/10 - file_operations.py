#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('[+] First Read')
with open('file.txt', 'r') as file:
    print(file.read())

print('\n[+] Second Read')
with open('file.txt', 'r') as file:
    while True:
        line = file.readline()
        print(line, end='')
        if not line:
            break

print('\n\n[+] Third Read')
with open('file.txt', 'r') as file:
    for line in file:
        print(line, end='')

print('\n\n[+] First Writing')
with open('file_output.txt', 'w') as file_output:
    data_to_write = 'Some text\n' * 100
    file_output.write(data_to_write)
    print('\t[|] Done writing file!')

data = {'ip': '127.0.0.1'}

print('\n\n[+] Second Writing')
with open('file_output_dict.txt', 'w') as file_output_dict:
    file_output_dict.write(str(data))
    print('\t[|] Done writing dict to a file!')

print('\n\n[+] Reading and Writing')
with open('file.txt', 'r') as file_input, open('file_output_2.txt', 'w') as file_output:
    file_output.write(file_input.read())
    print('\t[|] Done copying files!')