import socket

c = socket.socket()
c.connect(("12",9000))
 
broj1 = 6
broj2 = 8
znak = "*"

poruka = f"{broj1}|{broj2}|znak\n"

c.send(poruka.encode())
print(poruka)