import socket

c = socket.socket()
c.connect(("gresnik.com", 80))
zahtev = b"GET / HTTP/1.1\r\nHost: gresnik.com\r\n\r\n"
c.send(zahtev)
odgovor = c.recv(4096)
print(odgovor)
open("strana.html", "wb").write(odgovor)
