#!/usr/bin/env python3
import socket

HOST = '0.0.0.0'
PORT = 30001


class AsciiArt:
    def __init__(self):
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
                Enjoy Python Hacking!!!
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


message = AsciiArt()

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            print('[+] EX1 Server running waiting connections...')
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                conn.sendall(message.welcome)
                while True:
                    data = conn.recv(4096).decode()
                    print(data)
                    if 'Hello Word from Python Sockets!' in data:
                        conn.sendall(message.correct)
                        conn.close()
                        s.close()
                    else:
                        conn.sendall(message.wrong)
    except BrokenPipeError as error:
        pass
    except ConnectionAbortedError as error:
        pass
    except KeyboardInterrupt:
        print('CTRL+C pressed...')
        exit(0)
