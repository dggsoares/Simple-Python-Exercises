#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list1 = []
print(list1)
list2 = list()
print(list2)
list3 = [1, 2, 3, 4, 5]
print(list3)
list4 = ['One', 'Two', 'Three', 'Four', 'Five']
print(list4)
list5 = ['One', 2, 'Three', 4, 'Five']
print(list5)

string = 'Pythonic Way of Life!'
list_from_string = list(string)
print(list_from_string)

if list1:
    print('Not Empty')
else:
    print('Is empty')

print(f'Size of "list5": {len(list5)}')

list5.append(5)
list5.append('Six')

print(f'"list5" : {list5}')

list5.extend(list4)

print(f'"list5" : {list5}')

element = list5.pop()

print(f'"element" : {element}')
print(f'"list5" : {list5}')

list5.clear()

print(f'"list5" : {list5}')

# List comprehensions

aux_list = []
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    aux_list.append(x + 5)

print(f'"For" : {aux_list}')

print(f'List comprehensions: {[x + 5 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]}')

print(f'Using range(): {[x + 5 for x in range(11)]}')

aux_list_2 = []
for x in range(11):
    aux_list_2.append(x + 5)