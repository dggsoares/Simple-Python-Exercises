#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def create_key(password):
    salt = b'\x1b\xd1\x8ac\x83\x04\xed>\xb2\xaa\x9eH\x87\xfe\xf9\x19'  # os.random(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key


def main():
    password = 'PythonOffensiveClass'
    key = create_key(password.encode())

    #Files names
    file_name = 'top_secret_document.pdf'
    encrypted_file_name = 'top_secret_document_fernet_encrypted'

    # Encrypt file
    with open(file_name, 'rb') as file_input, open(encrypted_file_name, 'wb') as file_output:
        file_output.write(Fernet(key).encrypt(file_input.read()))


if __name__ == '__main__':
    main()
