#For Chat Sever Window
Encrypt: python encrypt.py

#For multiple clients
Terminal: python
          from socket import *
          s = socket()
          s.connect(('localhost', 8000))
          s.send('Message')

#For Users having pre-shared key
Decrypt: python decrypt.py
         Enter first pre-shared key: 737
         Enter second pre-shared key: 277
         
