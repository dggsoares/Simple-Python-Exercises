import socket
from threading import Thread
import random
import string
import base64

ADDRESS = ('178.128.157.183', 30001)


def gera_lixo():
    characters = string.ascii_letters + string.punctuation
    return base64.b64encode(''.join(random.choice(characters) for _ in range(20)).encode()).decode()


class ClientThread(Thread):

    def __init__(self):
        Thread.__init__(self)


    def run(client_id):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(ADDRESS)
        message = f'\n\tClient: {client_id} \n\tMESSAGE: {gera_lixo()}'
        s.send(message.encode())
        response = s.recv(2048).decode()
        print('--------------------------------------')
        print(f'Client {client_id}')
        print(f'SENT: {message}')
        print(f'RECV: {response}')
        print('--------------------------------------')


if __name__ == '__main__':

    clients_threads = []

    for i in range(10):
        client = ClientThread()
        client.start()
        clients_threads.append(client)

    for t in clients_threads:
        t.join()