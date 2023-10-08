import socket,os

server = socket.socket()
server.bind(("0.0.0.0",8000))
server.listen()
while True:
    klijent, adresa = server.accept()
    pitanje = klijent.recv(4096)
    delovi = pitanje.decode().strip().split(" ")
    fajl = delovi[1]
    fajl =  fajl.lstrip("/")


    if not fajl: 
        sadrzaj_fajla = open("index.html","r").read()
        odgovor = "HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n"
        odgovor = odgovor + sadrzaj_fajla
        klijent.send(odgovor.encode()) 
    else:
        if os.path.exists(fajl):
            sadrzaj_fajla = open(fajl,"r").read()
            odgovor = "HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n"
            odgovor = odgovor + sadrzaj_fajla
            klijent.send(odgovor.encode())
        else:
            odgovor = "HTTP/1.1 404 Not Found\r\n\r\n"
            klijent.send(odgovor.encode())
    klijent.close()