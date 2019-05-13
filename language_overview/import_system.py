#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import datetime

from math import cos
import math as mathematics

from requests import get as get_http

from oop_python import Robot

print(f'Current working directory: {os.getcwd()}')
print(f'Current time: {datetime.datetime.now()}')
print(f'Cosine : {cos(12345)}')
print(f'π = {mathematics.pi}')
print(f'HTTP Status code: {get_http("https://www.google.com").status_code}')

robot_1 = Robot('Bob', 'red')
robot_1.walk()
robot_1.talk()
robot_1.stop()