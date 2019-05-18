#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import base64

def xor(message, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(message, key)])


class MyHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "The Python Offensive Class"
        key = 'PythonOffensive201#@113445'
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        encrypted_message = xor(message, key)
        encoded_message = base64.b64encode(encrypted_message.encode())
        self.wfile.write(encoded_message)


server_adress = ('', 3321)
httpd = HTTPServer(server_adress, MyHTTPServer)
print('Running server...')
httpd.serve_forever()
