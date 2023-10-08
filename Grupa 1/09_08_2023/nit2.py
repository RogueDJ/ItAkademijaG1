import threading, time,socket

pesme = {
    "smoke":["A", "B", "C", "D", "A", "C", "E", "D", "A", "C", "D", "C", "A"],
    "smooth":["Dd", "Am", "Gm7", "Am7"],
    "take_on_me":["Am", "Cm", "Dm", "Gm"]
}
def pusti_pesmu(p):
    id_niti = threading.get_native_id()
    pesma = "smooth"
    pesma = pesme[p]
    for i in range(2):
        for nota in pesma:
            print(p,nota)
            time.sleep(1)

server = socket.socket()
server.bind(("0.0.0.0",8000))
server.listen()

klijent,adresa = server.accept()
while True:
    pesma = klijent.recv(1024).decode().strip()
    print(pesma)
# for p in pesme:
#     nit = threading.Thread(None, pusti_pesmu,args=(p,))
#     nit.start()