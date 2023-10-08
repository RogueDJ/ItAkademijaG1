from abc import *
import time
class Trening(ABC):
    def __init__(self, naziv, trajanje, kalorije):
        self.naziv = naziv
        self.trajanje = trajanje
        self.kalorije = kalorije

    def prikazi_opis(self):
        return f"Naziv:{self.naziv}\nTrajanje:{self.trajanje}min\nKalorije:{self.kalorije}kcal"
    @abstractmethod
    def zapocni_trening(self):
        pass

class Kardio(Trening):
    def zapocni_trening(self):
        print(f"Zapocet je trening:{self.naziv}")
        time.sleep(5)
        print(f"Zavrsen je trening. Potrosili ste {self.kalorije} kcal")


# kardio1 = Kardio("Trcanje", 60, 300)

# kardio1.zapocni_trening()

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        self.__jmbg = ""

    # def get_jmbg(self):
    #     if self.__jmbg !="":
    #         # 1234567891010
    #         # "123456789****"
    #         prvi_deo = self.__jmbg[0:9]
    #         izlaz = prvi_deo + "****"
    #         return izlaz
    #     else:
    #         print("Nije postavljen JMBG")
    @property
    def jmbg(self):
        if self.__jmbg !="":
            # 1234567891010
            # "123456789****"
            prvi_deo = self.__jmbg[0:9]
            izlaz = prvi_deo + "****"
            return izlaz
        else:
            print("Nije postavljen JMBG")    

    @jmbg.setter
    def set_jmbg(self, vrednost):
        if isinstance(vrednost, str):
            if len(vrednost) == 13:
                self.__jmbg = vrednost
            else:
                print("JMBG mora da ima 13 karaktera")
        else:
            print("Podatak mora da bude string tipa")

o = Osoba("Sofija", "Sofilic")
# print(o.__jmbg)
# print(o.get_jmbg())
# o.set_jmbg("1234567891010")
o.jmbg = "1234567891010"
# print(o.get_jmbg())
print(o.jmbg)
