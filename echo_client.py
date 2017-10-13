#! /usr/bin/python
# echo_client.py
import socket
host = "127.0.0.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b"Hello Python!")
data = s.recv(1024)
print("Recieved data:", data)
s.close()
