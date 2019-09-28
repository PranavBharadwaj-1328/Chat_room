import socket
import os

s = socket.socket()
os.system('figlet socket is set')

host = '10.5.1.92'
port = 1234


s.bind((host,port))
print ("socket: %s"%(port))
s.listen(5)
print ("heard")

while True:
    c, addr = s.accept()
    print ('connection established with', addr)
    a = 'figlet u are connected to server'
    #a = str(a)
    b = a.encode()
    c.send(b)
    c.close()
