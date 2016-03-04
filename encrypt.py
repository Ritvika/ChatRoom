import sys
import os
import socket
import SocketServer
from threading import Thread
import threading

def clientHandler():
    conn, addr = s.accept()
    print 'New User ', addr, 'is Connected'
    while 1:
        data = conn.recv(1024)
        if not data:
           break
        k1, k2 = 277, 737
        words = data;
	encrypt_data = "";
	for i in range(0, len(words)) :
		encrypt_data += str(encryption(ord(words[i]), k2, k1)) + ","
        print 'New message from User ', addr, ': ', repr(encrypt_data)

def encryption(x, e, c) :
	return ((int(x)**int(e)) % int(c))

HOST = ''
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print 'Chat Room is open. Waiting for users to connect....'

for i in range(5):
    Thread(target=clientHandler).start()

s.close()
