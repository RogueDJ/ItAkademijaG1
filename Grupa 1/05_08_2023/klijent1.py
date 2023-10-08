import socket

c = socket.socket(type=socket.SOCK_DGRAM)

c.sendto(b"dobar dan", ("127.0.0.1",9000))