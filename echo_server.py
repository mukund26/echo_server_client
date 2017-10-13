#! /usr/bin/python
# echo_server.py
import socket
import sys

def pad(s, n):
	nsp = n - len(s) - 10
	rs = "[ :: " + s
	for i in range(nsp):
		rs = rs + " "
	rs = rs + ":: ]"
	return rs;

def dummy_pad(dummy, s, n):
	ld = len(dummy) + 1
	nsp = n - ld - len(s) - 5;
	rs = s;
	for i in range(nsp):
		rs = rs + " "
	rs = rs + ":: ]"
	return rs


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

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print center("server is now listening on host " + host + ", port " + str(port), 70)
print

while True:
    conn, addr = s.accept()
    
    claddr = str(addr[0])
    clport = str(addr[1])
    print pad("client connected -- ip " + claddr + ", port " + clport, 70)
    
    data = conn.recv(1024)
    if not data:
        break
    
    datasize = str(sys.getsizeof(data))
    print pad("data received -- " + datasize + " bytes", 70)
    print "[ :: sending response...",
    conn.sendall(data)
    print dummy_pad("[ :: sending response...", " done!", 70)
    print

conn.close()



