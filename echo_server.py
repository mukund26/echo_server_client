#! /usr/bin/python
# echo_server.py
import socket
import sys
host = "127.0.0.1"
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
    conn, addr=s.accept()
    print('Connected by :',addr)
    data = conn.recv(1024)
    if not data:
        break
    print(sys.getsizeof(data))
    conn.sendall(data)
conn.close()



