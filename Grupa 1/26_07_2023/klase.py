class Automobil:
    def __init__(self, marka, model, godiste, parkiran = False):
        self.marka = marka
        self.model = model
        self.godiste = godiste
        self.parkiran = parkiran

    def informacije(self):
        status = "Parkiran" if self.parkiran else "U Pokretu"
        return f"Marka:{self.marka}\nModel:{self.model}\nGodiste:{self.godiste}\n{status}"
    
    @staticmethod
    def info_o_automobilu():
        print("Automobili imaju 4 tocka")
        print("Automobili se registruju jednom godisnje")

    def parkiraj(self):
        if self.parkiran == True:
            print("Vec ste parkirani")
        else:
            self.parkiran = True
            print("Parkirani ste")

automobil1 = Automobil("Audi", "C4", 2008, True)
print(f"Marka:{automobil1.marka}")

print(automobil1.informacije())

automobil2 = Automobil("Ford", "Forge", 2014, False)

print(automobil2.informacije())
print(Automobil.info_o_automobilu())
automobil1.parkiraj()
