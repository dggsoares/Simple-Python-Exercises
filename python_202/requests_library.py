#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

URL = "http://maps.googleapis.com/maps/api/geocode/json"

location = "Massachusetts Institute of Technology"

params = {'address': location}

r = requests.get(url=URL, params=params)

data = r.text

print(data)
