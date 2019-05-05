from socketserver import BaseRequestHandler


class Exercise(BaseRequestHandler):
    def handle(self):
        pass


class Ex14(Exercise):
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
                Enjoy Offensive Python!!!
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


class Ex15(Exercise):
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
                Enjoy Offensive Python!!!
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


class Ex16(Exercise):
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
                Enjoy Offensive Python!!!
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
