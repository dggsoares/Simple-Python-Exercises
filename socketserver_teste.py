import logging
import threading
import socketserver
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] PID: %(process)d - %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S'
                    )


class CustomTCPServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = f'{cur_thread.getName()}: {data}'.encode()
        self.request.send(response)
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
        thread.setDaemon(True)
        thread.start()
        logging.debug(f'{thread.getName()} is run on port: {server.server_address}')
        custom_tcp_servers_threads.append(thread)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt as e:
            logging.info('Shutting down servers...')
            for server in custom_tcp_servers:
                server.shutdown()
            for thread in custom_tcp_servers_threads:
                thread.join()
