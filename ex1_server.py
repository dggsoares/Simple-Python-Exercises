import coloredlogs, logging
import threading
import socketserver
import time
import sys

from exercises import *

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG',
                    logger=logger,
                    fmt='%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S'
                    )


class CustomTCPServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        exercise = Ex14()
        self.request.send(exercise.welcome)
        data = self.request.recv(2048).decode()
        cur_thread = threading.currentThread().getName()
        client_ip, client_port = self.client_address
        logger.info(f'Client IP {client_ip}:{client_port} is connected in thread: {cur_thread} on port: XX')
        if data == exercise.answer:
            self.request.send(exercise.correct)
            logger.info(f'Client IP {client_ip}:{client_port}, CORRECT')
        else:
            self.request.send(exercise.wrong)
            logger.info(f'Client IP {client_ip}:{client_port}, WRONG "{data}"')
        return


class CustomTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def __init__(self, server_address, handler_class):
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        socketserver.TCPServer.allow_reuse_address = True
        socketserver.ThreadingMixIn.daemon_threads = True
        return


if __name__ == '__main__':

    custom_tcp_servers = []
    custom_tcp_servers_threads = []

    for port in range(30000, 30011):
        server = CustomTCPServer(('', port), CustomTCPServerHandler)
        custom_tcp_servers.append(server)
        thread = threading.Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()
        logger.debug(f'{thread.getName()} is run on port: {server.server_address}')
        custom_tcp_servers_threads.append(thread)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt as e:
            logger.info('Shutting down servers...')
            sys.exit(0)
