import sys
import os
import socket
import SocketServer
import threading

def decryption(message, k1, k2) :
	text = message.split(",");
	decrypt_data = "";
	for i in range(0, len(text)-1) :
		decrypt_data += str(decode(encryption(text[i], k1, k2)))
	return decrypt_data

def key() :
	k1 = int(raw_input("\nEnter first pre-shared key: "))
	k2= int(raw_input("Enter second pre-shared key: "))
	message = str(raw_input("Enter message to decrypt: "))
	print "Decrypted message:"
	print decryption(message, k1, k2)

def encryption(x, e, c) :
	return ((int(x)**int(e)) % int(c))

def decode(x) :
	try :
		return str(unichr(x))
	except ValueError :
		print "** ERROR - Decoded character is unrecognized **"

def main() :
	while(1) :
		key()

main()

