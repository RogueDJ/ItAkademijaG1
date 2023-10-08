class automobil:
    marka = ""
    model = ""
    godiste = 0
    alu_felne = False
    broj_tockova = 4

    def vozi(self):
        print("Auto je u pokretu")
        print(self.model)

    def postavi_felne(self):
        if self.alu_felne == True:
            print("Imate vec alu felne")
        else:
            self.alu_felne = False

    def __init__(self, zeljena_marka, zeljeni_model, god, alu_felne):
        print("Pravim automobil")
        self.marka = zeljena_marka
        self.model = zeljeni_model
        self.godiste = god
        self.alu_felne = alu_felne

a = automobil("Citroen", "C4" , 2018, True)


class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

osoba1 = Osoba("Milka", "Kravica", 23)
print(osoba1.ime, osoba1.prezime, osoba1.godine)