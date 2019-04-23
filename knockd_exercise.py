import socket

host = '192.168.246.128'
ports = [7000, 8000, 9000]
# ports = [9000, 8000, 7000]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    s.connect_ex((host, port))
    s.close()
w