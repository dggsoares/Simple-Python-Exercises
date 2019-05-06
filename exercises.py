import socketserver
import threading

from custom_logger import *


class Exercise(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        return


class Ex14(Exercise):
    def __init__(self, request, client_address, server):
        self.name = 'Ex14'
        self.description = 'Echo Server with Sockets'
        self.welcome = '''\
                         uuuuuuu
                     uu$$$$$$$$$$$uu
                  uu$$$$$$$$$$$$$$$$$uu
                 u$$$$$$$$$$$$$$$$$$$$$u
                u$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$"   "$$$"   "$$$$$$u
               "$$$$"      u$u       $$$$"
                $$$u       u$u       u$$$
                $$$u      u$$$u      u$$$
                 "$$$$uu$$$   $$$uu$$$$"
                  "$$$$$$$"   "$$$$$$$"
                    u$$$$$$$u$$$$$$$u
                     u$"$"$"$"$"$"$u
          uuu        $$u$ $ $ $ $u$$       uuu
         u$$$$        $$$$$u$u$u$$$       u$$$$
          $$$$$uu      "$$$$$$$$$"     uu$$$$$$
        u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
        $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
          """      ""$$$$$$$$$$$uu ""$"""
                   uuuu ""$$$$$$$$$$uuu
          u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
          $$$$$$$$$$""""           ""$$$$$$$$$$$"
          "$$$$$"                      ""$$$$""
            $$$"                         $$$$"

    Welcome to IV International Cyber Defense Course
                Enjoy Offensive Python!!!
         EXERCISE 1.4 - Echo Server With Sockets
'''.encode()
        self.wrong = '''\
    +---------------------------------------------+
    |        INCORRECT MESSAGE, TRY AGAIN! :(     |
    +---------------------------------------------+
        '''.encode()
        self.correct = '''\
    +---------------------------------------------+
    |               CORRECT MESSAGE! :)           |
    +---------------------------------------------+
    | The Flag is: PYTHON{P1th0nH3llOFromS0CK3T$} |
    +---------------------------------------------+
'''.encode()
        self.answer = 'Hello Word!'
        Exercise.__init__(self, request, client_address, server)

    def handle(self):
        self.request.send(self.welcome)
        data = self.request.recv(2048).decode()
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(
            f'{self.name} | {client_ip}:{client_port} is connected in {cur_thread} on port: '
            f'{self.server.server_address[1]}')
        if data == self.answer:
            self.request.send(self.correct)
            logger.info(f'{self.name} | {client_ip}:{client_port}, CORRECT!')
        else:
            self.request.send(self.wrong)
            logger.info(f'{self.name} | {client_ip}:{client_port}, WRONG "{data}"')
        return


class Ex15(Exercise):
    def __init__(self, request, client_address, server):
        self.name = 'Ex15'
        self.description = 'Base64 Decode?'
        self.welcome = '''\
                         .88888888:.
                        88888888.88888.
                      .8888888888888888.
                      888888888888888888
                      88' _`88'_  `88888
                      88 88 88 88  88888
                      88_88_::_88_:88888
                      88:::,::,:::::8888
                      88`:::::::::'`8888
                     .88  `::::'    8:88.
                    8888            `8:888.
                  .8888'             `888888.
                 .8888:..  .::.  ...:'8888888:.
                .8888.'     :'     `'::`88:88888
               .8888        '         `.888:8888.
              888:8         .           888:88888
            .888:88        .:           888:88888:
            8888888.       ::           88:888888
            `.::.888.      ::          .88888888
           .::::::.888.    ::         :::`8888'.:.
          ::::::::::.888   '         .::::::::::::
          ::::::::::::.8    '      .:8::::::::::::.
         .::::::::::::::.        .:888:::::::::::::
         :::::::::::::::88:.__..:88888:::::::::::'
          `'.:::::::::::88888888888.88:::::::::'
                `':::_:' -- '' -'-' `':_::::'`

                 EXERCISE 1.5 - Base64 Decode?
    '''.encode()
        self.wrong = '''\
        +---------------------------------------------+
        |        INCORRECT MESSAGE, TRY AGAIN! :(     |
        +---------------------------------------------+
            '''.encode()
        self.correct = '''\
        +-------------------------------------------------+
        |                CORRECT MESSAGE! :)              |
        +-------------------------------------------------+
        | The Flag is: PYTHON{P1th0nGr@tzf0rB@se64dec0d3} |
        +-------------------------------------------------+
    '''.encode()
        self.answer = 'XXXXXX'  # TODO criar lógica do exercício
        Exercise.__init__(self, request, client_address, server)

    def handle(self):
        self.request.send(self.welcome)
        data = self.request.recv(2048).decode()
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(
            f'{self.name} | {client_ip}:{client_port} is connected in {cur_thread} on port: '
            f'{self.server.server_address[1]}')
        if data == self.answer:
            self.request.send(self.correct)
            logger.info(f'{self.name} | {client_ip}:{client_port}, CORRECT!')
        else:
            self.request.send(self.wrong)
            logger.info(f'{self.name} | {client_ip}:{client_port}, WRONG "{data}"')
        return


class Ex16(Exercise):
    def __init__(self, request, client_address, server):
        self.name = 'Ex16'
        self.description = 'Math!'
        self.welcome = '''\
                           _____
                         .'/L|__`.
                        / =[_]O|` \\
                        |"+_____":|
                      __:='|____`-:__
                     ||[] ||====| []||
                     ||[] | |=| | []||
                     |:||_|=|U| |_||:|
                     |:|||]_=_ =[_||:|
                     | |||] [_][]C|| |
                     | ||-'"""""`-|| |
                     /|\\_\_|_|_/_//|\\
                    |___|   /|\   |___|
                    `---'  |___|  `---'
                           `---'
                EXERCISE 1.6 - Math Using Sockets!
    '''.encode()
        self.wrong = '''\
        +---------------------------------------------+
        |        INCORRECT MESSAGE, TRY AGAIN! :(     |
        +---------------------------------------------+
            '''.encode()
        self.correct = '''\
        +----------------------------------------------+
        |               CORRECT MESSAGE! :)            |
        +----------------------------------------------+
        | The Flag is: PYTHON{P1th0nDoM@thwithS0ck3t$} |
        +----------------------------------------------+
    '''.encode()
        self.answer = 'XXXX'  # TODO fazer a lógica do exercício
        Exercise.__init__(self, request, client_address, server)

    def handle(self):
        self.request.send(self.welcome)
        data = self.request.recv(2048).decode()
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(
            f'{self.name} | {client_ip}:{client_port} is connected in {cur_thread} on port: '
            f'{self.server.server_address[1]}')
        if data == self.answer:
            self.request.send(self.correct)
            logger.info(f'{self.name} | {client_ip}:{client_port}, CORRECT!')
        else:
            self.request.send(self.wrong)
            logger.info(f'{self.name} | {client_ip}:{client_port}, WRONG "{data}"')
        return
