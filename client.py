import socket

s = socket.socket()
s.connect(('10.5.1.92',1234))
while True:
  data = input('->')
  data = str(data)
  s.send(data.encode())
  print(s.recv(1024).decode())
  if(str(s.recv(1024).decode()) == "bye"):
    s.close()
    break
