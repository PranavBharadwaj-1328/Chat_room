import socket
import os

s = socket.socket()
os.system('figlet socket is set')

host = '<client ip>'
port = 'port no.'


s.bind((host,port))
print ("socket: %s"%(port))
s.listen(5)
print ("heard")
c, addr = s.accept()
print ('connection established with', addr)
while True:
    d = str(c)
    #a = 'Hi %s are connected to PB server'%d
    data = c.recv(1024).decode()
    if(str(data) == 'bye'):
      c, addr = s.accept()
      print ('connection established with', addr)
      continue
    print ("Recieved from the above client:"+str(data))
    data = input('->')
    c.send(data.encode())


