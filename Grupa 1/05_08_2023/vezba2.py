import socket

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9000))

paket, adresa = s.recvfrom(128)
print(paket, adresa)