import socket

s = socket.socket()

s.connect(('10.5.1.92',1234))

print(s.recv(1024))

s.close()
