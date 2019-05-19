#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('Number sequence: ')
for number in [1, 2, 3, 4, 5, 6]:
    print(number)

print('\nNumber sequence with range(): ')

for number in range(1, 7):
    print(number)

print('\nIterating over sequence')
print('Names:')
names = ['Bob', 'Maroon', 'Damian']

for name in names:
    print('\t' + name)

print('\nIterating over sequence with enumerate()')
print('Names:')
for index, name in enumerate(names):
    print(f'\t{index} : {name}')