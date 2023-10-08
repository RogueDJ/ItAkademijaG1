import socket

c = socket.socket()
c.connect(("127.0.0.1",9000))
c.send(b"GET /lol.txt HTTP/1.1")
zaglavlje = c.recv(2000)
print(zaglavlje)
fajl = c.recv(2000)
print(fajl)
