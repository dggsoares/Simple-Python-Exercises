from exercises.exercises import *

ZEN_OF_PYTHON = [
    'Beautiful is better than ugly.',
    'Explicit is better than implicit.',
    'Simple is better than complex.',
    'Complex is better than complicated.',
    'Flat is better than nested.',
    'Sparse is better than dense.',
    'Readability counts.',
    "Special cases aren't special enough to break the rules.",
    'Although practicality beats purity.',
    'Errors should never pass silently.',
    'Unless explicitly silenced.',
    'In the face of ambiguity, refuse the temptation to guess.',
    'There should be one-- and preferably only one --obvious way to do it.',
    "Although that way may not be obvious at first unless you're Dutch.",
    'Now is better than never.',
    'Although never is often better than *right* now.',
    "If the implementation is hard to explain, it's a bad idea.",
    'If the implementation is easy to explain, it may be a good idea.',
    "Namespaces are one honking great idea -- let's do more of those!"
]


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
        # Client logging
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(
            f'{self.name} | {client_ip}:{client_port} is connected in {cur_thread} on port: '
            f'{self.server.server_address[1]}')

        self.request.send(self.welcome)  # Welcome message
        data = self.request.recv(2048).decode()  # Client response

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
        self.welcome = '''
                     ---_ ......._-_--.
                    (|\ /      / /| \\
                    /  /     .'  -=-'   `.
                   /  /    .'             )
                 _/  /   .'        _.)   /
                / o   o        _.-' /  .'
                \          _.-'    / .'*|
                 \______.-'//    .'.' \*|
                  \|  \ | //   .'.' _ |*|
                   `   \|//  .'.'_ _ _|*|
                    .  .// .'.' | _ _ \*|
                    \`-|\_/ /    \ _ _ \*
                    `/'\__/       \ _ _ \*
                    /^|            \ _ _ \*
                   '  `             \ _ _\_
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
        self.answer = ''
        Exercise.__init__(self, request, client_address, server)

    def handle(self):
        # Client logging
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(
            f'{self.name} | {client_ip}:{client_port} is connected in {cur_thread} on port: '
            f'{self.server.server_address[1]}')

        self.request.send(self.welcome)
        self.request.send(self.create_prhase())  # Phrase challenge
        data = self.request.recv(1024).decode()  # Client response

        if data == self.answer:
            self.request.send(self.correct)
            logger.info(f'{self.name} | {client_ip}:{client_port}, CORRECT!')
        else:
            self.request.send(self.wrong)
            logger.info(f'{self.name} | {client_ip}:{client_port}, WRONG "{data}"')
        return

    def create_prhase(self):
        phrase = random.choice(ZEN_OF_PYTHON)
        self.answer = phrase[:10]
        return base64.b64encode(phrase.encode())


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
             operators = ['+', '-', '*', '/']
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
        self.answer = ''
        Exercise.__init__(self, request, client_address, server)

    def handle(self):
        # Client logging
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(
            f'{self.name} | {client_ip}:{client_port} is connected in {cur_thread} on port: '
            f'{self.server.server_address[1]}')

        self.request.send(self.welcome)  # Welcome message

        self.request.send(self.create_challenge())  # First Challenge
        first_response = self.request.recv(1024).decode()  # Client response

        if first_response == self.answer:
            logger.info(f'{self.name} | {client_ip}:{client_port}, step 1 CORRECT!')
            self.request.send(self.create_challenge())  # Second challenge
            second_response = self.request.recv(1024).decode()  # Client response

            if second_response == self.answer:
                logger.info(f'{self.name} | {client_ip}:{client_port}, step 2 CORRECT!')
                self.request.send(self.create_challenge())  # Three challenge
                third_response = self.request.recv(1024).decode()  # Client response

                if third_response == self.answer:
                    logger.info(f'{self.name} | {client_ip}:{client_port}, step 3 CORRECT!')
                    self.request.send(self.correct)  # Correct answer for challenge

        else:
            self.request.send(self.wrong)
        return

    def create_challenge(self):
        operators = ['+', '-', '*', '/']
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        operator = random.choice(operators)
        self.answer = str(eval(f'{a}{operator}{b}'))
        expression = f'{a}&{b}&{operator}'
        return expression.encode()


class SocketSample(Exercise):
    def __init__(self, request, client_address, server):
        self.name = 'SocketSample'
        self.description = 'Just a socket sample!'
        self.welcome = random.choice(ZEN_OF_PYTHON).encode()
        Exercise.__init__(self, request, client_address, server)

    def handle(self):
        # Client logging
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(
            f'{self.name} | {client_ip}:{client_port} is connected in {cur_thread} on port: '
            f'{self.server.server_address[1]}')

        self.request.send(self.welcome)  # Just send welcome message
        return