#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Hello world from My HTTP Server!"
        self.wfile.write(message.encode())


server_adress = ('', 32001)
httpd = HTTPServer(server_adress, MyHTTPServer)
print('Running server...')
httpd.serve_forever()
