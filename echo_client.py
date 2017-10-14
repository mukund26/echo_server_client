#! /usr/bin/python
# echo_client.py
import socket

def pad(s, n):
	nsp = n - len(s) - 10
	rs = "[ :: " + s
	for i in range(nsp):
		rs = rs + " "
	rs = rs + ":: ]"
	return rs;

def center(s, n):
	nsp = n - len(s) - 12
	rs = "[ ... ";
	for i in range(nsp/2):
		rs = rs + " "
	rs = rs + s;
	for i in range(nsp/2):
		rs = rs + " "

	if (nsp % 2 != 0):
		rs = rs + " "

	rs = rs + "... ]"
	return rs;

host = "127.0.0.1"
port = 12345
data = "Hello Python!"

print center("connecting to host " + host + ", port " + str(port), 70)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print pad("sending data to host: " + data, 70)
s.sendall(data)
print pad("receiving data from host " + host + ", port " + str(port), 70)
data = s.recv(1024)

print pad("received data: " +str(data), 70)

s.close()
