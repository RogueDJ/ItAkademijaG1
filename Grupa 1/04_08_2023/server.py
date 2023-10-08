import socket
server = socket.socket()
server.bind(("0.0.0.0",8000))
server.listen()
while True:

    klijent,adresa = server.accept()
    pitanje = klijent.recv(128)
    print(pitanje)
    klijent.close()