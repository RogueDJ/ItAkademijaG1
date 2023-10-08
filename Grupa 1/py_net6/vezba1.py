import threading, time

kljuc = threading.Lock()
class Vozilo(threading.Thread):
    def __init__(self,tip, brzina):
        self.tip =          tip
        self.brzina =       brzina
        self.destinacija =    0
        self.trenutna_tacka = 0
        super().__init__()

    def run(self):
        while self.trenutna_tacka < self.destinacija:
            kljuc.acquire()
            print(f"{self.tip} je na poziciji {self.trenutna_tacka}")
            kljuc.release()
            self.trenutna_tacka += self.brzina
            time.sleep(0.5)
        kljuc.acquire()
        print(self.tip, "je stigao")
        kljuc.release()



    def kreni(self, destinacija):
        self.destinacija = destinacija
        self.trenutna_tacka = 0
        self.start()


class Auto(Vozilo):
    def __init__(self):
        super().__init__("Auto", 150)

class Kamion(Vozilo):
    def __init__(self):
        super().__init__("Kamion", 100)

a = Auto()
k = Kamion()
a.kreni(1200)
k.kreni(800)