# https://pymotw.com/3/socketserver/

import logging
import socketserver
import threading

logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s', )


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        self.logger.debug('setup')
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):
        self.logger.debug('handle')

        data = self.request.recv(2048).decode()
        cur_thread = threading.currentThread()
        response = f'\n\tThread: {cur_thread.getName()} {data}'.encode()
        self.logger.debug(f'recv()->"{data}"')
        self.logger.debug(f'answer: "{response}"')
        self.request.send(response)
        return

    def finish(self):
        self.logger.debug('finish')
        return socketserver.BaseRequestHandler.finish(self)


class EchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def __init__(self, server_address,
                 handler_class=EchoRequestHandler,
                 ):
        self.logger = logging.getLogger('EchoServer')
        self.logger.debug('__init__')
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        return

    def server_activate(self):
        self.logger.debug('server_activate')
        socketserver.TCPServer.server_activate(self)
        return

    def serve_forever(self, poll_interval=0.5):
        self.logger.debug('waiting for request')
        self.logger.info('Handling requests, press <Ctrl-C> to quit')
        socketserver.TCPServer.serve_forever(self, poll_interval)
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        self.logger.debug('verify_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.verify_request(self, request, client_address, )

    def process_request(self, request, client_address):
        self.logger.debug('process_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.process_request(self, request, client_address, )

    def server_close(self):
        self.logger.debug('server_close')
        return socketserver.TCPServer.server_close(self)

    def finish_request(self, request, client_address):
        self.logger.debug('finish_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.finish_request(self, request, client_address, )

    def close_request(self, request_address):
        self.logger.debug('close_request(%s)', request_address)
        return socketserver.TCPServer.close_request(self, request_address, )

    def shutdown(self):
        self.logger.debug('shutdown()')
        return socketserver.TCPServer.shutdown(self)


if __name__ == '__main__':
    address = ('localhost', 30001)  # let the kernel assign a port
    server = EchoServer(address, EchoRequestHandler)
    server.serve_forever()

    # ip, port = server.server_address  # what port was assigned?
    # # Start the server in a thread
    # t = threading.Thread(target=server.serve_forever)
    # t.setDaemon(True)  # don't hang on exit
    # t.start()
    # print(f'Server loop running in thread: {t.getName()}')
