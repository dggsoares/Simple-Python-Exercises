#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

URL = "https://www.us-cert.gov/ncas/alerts/2014"

r = requests.get(url=URL)
soup = BeautifulSoup(r.text, 'html.parser')
alerts = soup.select('.item-list ul li')
for alert in alerts:
    id = alert.find('span', {'class': 'document_id'}).string
    title = alert.find('span', {'class': 'document_title'}).string
    print(id + title)

print(f'Total Alerts: {len(alerts)}')