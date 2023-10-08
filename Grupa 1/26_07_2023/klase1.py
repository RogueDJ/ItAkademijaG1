class Aplikacija:
    def __init__(self, tip, broj_korisnika, mockup = True, preuzeta_za_rad = False):
        self.tip = tip
        self.broj_korisnika = broj_korisnika
        self.mockup = mockup
        preuzeta_za_rad = preuzeta_za_rad
    
app1 = Aplikacija("mobilna", 20, False, False) 
app2 = Aplikacija("Android", 40, True, True)
app3 = Aplikacija("Windows", 1000, True, False)



class Firma:
    def __init__(self, ime_kompanije, broj_zaposlenih, registrovana = True):
        self.ime_kompanije = ime_kompanije
        self.broj_zaposlenih = broj_zaposlenih
        self.registrovana = registrovana

    def otpusti_ljude(self, broj_otpustenih):
        if broj_otpustenih > self.broj_zaposlenih:
            print("Previse za otpustanje")
        else:
            if broj_otpustenih > 0:
                self.broj_zaposlenih -= broj_otpustenih
            else: 
                print("Proverite broj, mora biti veci od nule")

    def preuzmi_projekat(self, projekat):
        if projekat.mockup:
            print(f"Preuzet je projekat {projekat.tip}")
            projekat.preuzeta_za_rad = True
        else: 
            print("Donesite i mockup")

firma1 = Firma("IT Akademija", 300, True)
firma1.otpusti_ljude(10)
print(firma1.broj_zaposlenih)
firma1.preuzmi_projekat(app2)