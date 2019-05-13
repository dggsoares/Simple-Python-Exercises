#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def do_print(string):
    print(string)


print(f'Function do_print(string):')
do_print(f'Testing functions on Python')
do_print(f'5 + 6 = {5 + 6}')


def add_numbers(x, y):
    result = x + y
    return result


print('\nFunction add_numbers(x, y):')
print(f'2 + 4 = {add_numbers(2, 4)}')
print(f'3 + 4 = {add_numbers(7, 8)}')


def do_math(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b


print('\nFunction do_math(a, b, operator):')
a = 34
b = 21
print(f'[+] Addition: {a} + {b} = {do_math(a, b, "+")}')
print(f'[+] Division: {a} / {b} = {do_math(a, b, "/")}')
print(f'[+] Subtraction: {a} - {b} = {do_math(a, b, "-")}')
print(f'[+] Multiplication: {a} * {b} = {do_math(a, b, "*")}')