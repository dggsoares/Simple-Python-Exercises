from cryptography.fernet import Fernet

print(f'[+++] Fernet Encryption/Decryption tool [+++]')
message = "I turned my phone on airplane mode and threw it in the air. Worst transformer ever."
print(f'\t[|] Message to encrypt: {message}')
key = Fernet.generate_key()
print(f'\t[|] Fernet key: {key}')
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(message.encode())
print(f'\t[|] Message encrypted: {cipher_text.decode()}')
plain_text = cipher_suite.decrypt(cipher_text)
print(f'\t[|] Message decrypted: {plain_text.decode()}')

#TODO criptografar um arquivo