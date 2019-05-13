#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('While 1')
count = 0
while True:
    count += 1
    print(f'Count: {count}')
    if count == 10:
        break

print('\nWhile 2')
count = 0
while count < 10:
    count += 1
    print(f'Count: {count}')

