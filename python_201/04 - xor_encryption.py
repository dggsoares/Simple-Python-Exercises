#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import random


def generate_key(length):
    characters = string.ascii_letters + string.punctuation
    return ''.join((random.choice(characters) for _ in range(length)))


def xor(message, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(message, key)])


def main():
    print(f'[+++] Simple XOR Encryption/Decryption [+++]')
    message = input(' [X] Message to encrypt: ')
    key = generate_key(len(message))
    encrypted_message = xor(message, key)
    decrypted_message = xor(encrypted_message, key)
    print(f'\t [|] Key: {key[:25]}')
    print(f'\t [|] Key size: {len(key)}')
    print(f'\t [|] Message: {message}')
    print(f'\t [|] Encrypted message: {encrypted_message}')
    print(f'\t [|] Decrypted message: {decrypted_message}')


if __name__ == '__main__':
    main()
