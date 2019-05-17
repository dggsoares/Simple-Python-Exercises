#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64


def write_keys_on_disk(private_key, public_key):
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('private_key.pem', 'wb') as f:
        f.write(pem_private)
    with open('public_key.pem', 'wb') as f:
        f.write(pem_public)


def load_keys_from_disk():
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return private_key, public_key


def create_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt_message(key, message):
    encrypted_message = key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message


def decrypt_message(key, message):
    original_message = key.decrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message


def encrypt_file(key, file):
    encrypted_file = bytes()
    chunk = 256
    with open(file, "rb") as f:
        while True:
            data = f.read(chunk)
            if data:
                encrypted_file += encrypt_message(key, base64.b64encode(data))
            else:
                break

    with open(file + '.enc', 'wb') as f:
        f.write(encrypted_file)


def decrypt_file(key, file):
    original_file = bytes()
    chunk = 256
    with open(file, "rb") as f:
        while True:
            data = f.read(chunk)
            if data:
                original_file += decrypt_message(key, data)
            else:
                break

    with open(file + '.original', 'wb') as f:
        f.write(original_file)


def main():
    private_key, public_key = create_keys()
    encrypt_file(public_key, 'file.txt')
    decrypt_file(private_key, 'file.txt.enc')
    # write_keys_on_disk(private_key, public_key)
    # private_key, public_key = load_keys_from_disk()
    # print(f'[+++] Simple RSA Encryption/Decryption [+++]')
    # message = input(' [X] Message to encrypt: ').encode()
    # encrypted_message = encrypt_message(public_key, message)
    # decrypted_message = decrypt_message(private_key, encrypted_message)
    # print(f'\t\t Message: {message}')
    # print(f'\t\t Encrypted message: {encrypted_message[:25]}')
    # print(f'\t\t Decrypted message: {decrypted_message}')


if __name__ == '__main__':
    main()
    #TODO criptografar uma mensagem