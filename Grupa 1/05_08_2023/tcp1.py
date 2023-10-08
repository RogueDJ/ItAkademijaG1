import socket
s = socket.socket()
s.bind(("0.0.0.0", 9000))
s.listen()
while True:
    c,a = s.accept()
    opis = c.recv(1024).decode()
    metod, of, verzija = opis.split(" ")
    of = of.strip("/")
    fajl = open(of, "rb")
    sadrzaj_fajla = fajl.read()
    opis_odgovora = f"{verzija} 200 OK\r\n\r\n"
    c.send(sadrzaj_fajla)
    c.send(opis_odgovora.encode())