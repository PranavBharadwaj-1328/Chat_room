import socket

s = socket.socket()
s.connect(('<server ip>','port no.'))
while True:
  data = input('->')
  data = str(data)
  s.send(data.encode())
  print(s.recv(1024).decode())
  if(str(s.recv(1024).decode()) == "bye"):
    s.close()
    break
