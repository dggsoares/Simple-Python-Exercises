import time

from exercises import *
from custom_logger import *


class CustomTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def __init__(self, server_address, handler_class):
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        socketserver.TCPServer.allow_reuse_address = True
        socketserver.ThreadingMixIn.daemon_threads = True
        return


def create_server_exercise(start, end, exercise):
    custom_tcp_servers = []
    custom_tcp_servers_threads = []

    for port in range(start, end + 1):
        server = CustomTCPServer(('', port), exercise)
        custom_tcp_servers.append(server)
        thread = threading.Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()
        custom_tcp_servers_threads.append(thread)

    logger.debug(f'{len(custom_tcp_servers_threads)} threads is running on ports: {start}-{end}')


if __name__ == '__main__':
    create_server_exercise(30000, 30010, Ex14)
    create_server_exercise(30020, 30030, Ex15)
    create_server_exercise(30040, 30050, Ex16)
    create_server_exercise(45000, 45010, SocketSample)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt as e:
            logger.info('Shutting down servers...')
            sys.exit(0)
