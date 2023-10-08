import threading, time

brava = threading.Lock()

class Film(threading.Thread):
    def __init__(self, naziv, trajanje):
        self.naziv = naziv
        self.trajanje = trajanje
        super().__init__()
    def run(self):
        brava.acquire()
        print(f"Emitovanje filma {self.naziv}")
        brava.release()
        for i in range(self.trajanje):
            brava.acquire()
            print(f"{self.naziv} : {i}min")
            brava.release()
            time.sleep(0.1)

f1 = Film("The road", 150)
f1.start()
f2 = Film("Idiocracy", 120)
f2.start()

