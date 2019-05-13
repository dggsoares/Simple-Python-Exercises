#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import logging
import coloredlogs
import sys
import socketserver
import threading

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG',
                    logger=logger,
                    fmt='%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',
                    stream=sys.stdout
                    )

class KnockdServer(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        self.name = 'Knockd Challenge'
        self.welcome = '''
                       u
                  .  x!X
                ."X M~~>
               d~~XX~~~k    .u.xZ `\ \ "%
              d~~~M!~~~?..+"~~~~~?:  "    h
             '~~~~~~~~~~~~~~~~~~~~~?      `
             4~~~~~~~~~~~~~~~~~~~~~~>     '
             ':~~~~~~~~~~(X+"" X~~~~>    xHL
              %~~~~~(X="      'X"!~~% :RMMMRMRs
               ^"*f`          ' (~~~~~MMMMMMMMMMMx
                 f     /`   %   !~~~~~MMMMMMMMMMMMMc
                 F    ?      '  !~~~~~!MMMMMMMMMMMMMM.
                ' .  :": "   :  !X""(~~?MMMMMMMMMMMMMMh
                'x  .~  ^-+="   ? "f4!*  #MMMMMMMMMMMMMM.
                 /"               .."     `MMMMMMMMMMMMMM
                 h ..             '         #MMMMMMMMMMMM
                 f                '          @MMMMMMMMMMM
               :         .:=""     >       dMMMMMMMMMMMMM
               "+mm+=~("           RR     @MMMMMMMMMMMMM"
                       %          (MMNmHHMMMMMMMMMMMMMMF
                      uR5         @MMMMMMMMMMMMMMMMMMMF
                    dMRMM>       dMMMMMMMMMMMMMMMMMMMF
                   RM$MMMF=x..=" RMRM$MMMMMMMMMMMMMMF
                  MMMMMMM       'MMMMMMMMMMMMMMMMMMF
                 dMMRMMMK       'MMMMMMMMMMMMMMMMM"
                 RMMRMMME       3MMMMMMMMMMMMMMMM
                @MMMMMMM>       9MMMMMMMMMMMMMMM~
               'MMMMMMMM>       9MMMMMMMMMMMMMMF
               tMMMMMMMM        9MMMMMMMMMMMMMM
               MMMM$MMMM        9MMMMMMMMMMMMMM
              'MMMMRMMMM        9MMMMMMMMMMMMM9
              MMMMMMMMMM        9MMMMMMMMMMMMMM
              RMMM$MMMMM        9MMMMMMMMMMMMMM
             tMMMMMMMMMM        9MMMMMMMMMMMMMX
             RMMMMMMMMMM        9MMMMMMMMMMMMME
            JMMMMMMMMMMM        MMMMMMMMMMMMMME
            9MMMM$MMMMMM        RMMMMMMMMMMMMME
            MMMMMRMMMMMX        RMMMMMMMMMMMMMR
            RMMMMRMMMMME        EMMMMMMMMMMMMM!
            9MMMMMMMMMME        MMMMMMMMMMMMMM>
            
                [+] KNOCKD CHALLENGE [+] {
                       YOU DID IT!
                    CONGRATULATIONS!
                }
            '''.encode()
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def handle(self):
        # Client logging
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(
            f'{self.name} | {client_ip}:{client_port} is connected in {cur_thread} on port: '
            f'{self.server.server_address[1]}')

        self.request.send(self.welcome)  # Just send welcome message
        return


class CustomTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def __init__(self, server_address, handler_class):
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        socketserver.TCPServer.allow_reuse_address = True
        socketserver.ThreadingMixIn.daemon_threads = True
        return


def create_server_exercise(port, exercise):
    custom_tcp_servers = []
    custom_tcp_servers_threads = []

    server = CustomTCPServer(('', port), exercise)
    custom_tcp_servers.append(server)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    custom_tcp_servers_threads.append(thread)

    logger.debug(f'{len(custom_tcp_servers_threads)} threads is running on port: {port}')


if __name__ == '__main__':
    create_server_exercise(6667, KnockdServer)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt as e:
            logger.info('Shutting down servers...')
            sys.exit(0)
