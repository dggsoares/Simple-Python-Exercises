import string
import random


def generate_key():
    characters = string.ascii_letters + string.punctuation
    return ''.join((random.choice(characters) for _ in range(512)))


def xor(message, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(message, key)])

def main():
    key = generate_key()
    print(f'[+++] Simple XOR Encryption/Decryption [+++]')
    message = input(' [X] Message to encrypt: ')
    encrypted_message = xor(message, key)
    decrypted_message = xor(encrypted_message, key)
    print(f'\t\t Key: "{key[:25]}" truncated...')
    print(f'\t\t Key size: {len(key)}')
    print(f'\t\t Message: {message}')
    print(f'\t\t Encrypted message: {repr(encrypted_message)}')
    print(f'\t\t Decrypted message: {(xor(encrypted_message, key))}')


if __name__ == '__main__':
    main()