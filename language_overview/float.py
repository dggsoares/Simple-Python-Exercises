#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Basic float operations')
a = 2.3
b = 3.4
addition = a + b
subtraction = a - b
multiplication = a * b
division = a * b
modulo = a % b
print(f'a = {a}')
print(f'b = {b}')
print(f'a + b = {addition}')
print(f'a - b = {subtraction}')
print(f'a * b = {multiplication}')
print(f'a / b = {division}')
print(f'a % b = {modulo}')

print('\nRound float')
x = 14.78945121
print(f'x = {x}')
print(f'x = {round(x, 2)}')
print('x = %.2f' % x)
