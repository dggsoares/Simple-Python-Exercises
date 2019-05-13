#!/usr/bin/env python3
# -*- coding: utf-8 -*-

run = True

if run:
    print("I'm running!")

sleep = False

if sleep:
    print("I'm sleeping!")
else:
    print("I'm not sleeping!")

aux = 9

if aux == 15:
    print('"Aux" equals 15')
elif aux == 14:
    print('"Aux" equals 14')
elif aux <= 12 and aux >= 10:
    print('"Aux" is between 10 and 12')
else:
    print('"Aux" is under 10')