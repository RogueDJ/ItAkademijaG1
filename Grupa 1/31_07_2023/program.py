import enum
class tipovi_skolovanja(enum.Enum):
    ONLINE = "online"
    TRADICIONALNO = "trad"

print(tipovi_skolovanja.ONLINE.value)
print(tipovi_skolovanja.TRADICIONALNO.name)


class Korisnik:
    def __init__(self, ime, tipSkolovanja):
        self.ime = ime
        self.tipSkolovanja = tipSkolovanja

kor1 = Korisnik("Sofija", tipovi_skolovanja.ONLINE)
print(kor1.ime, kor1.tipSkolovanja.value)

class Pol(enum.Enum):
    MUSKI = "m"
    ZENSKI = "z"

class TipoviPlacanja(enum.Enum):
    KES = 1
    KARTICA = 2
    CEKOVI = 3
    def __str__(self):
        return f"Naziv:{self.name}, vrednost: {self.value}"
    
print(TipoviPlacanja.KES)

for tip in TipoviPlacanja:
    print(tip)

odabrano = int(input("Odaberite nacin placanja - KES: 1, KARTICA: 2, CEKOVI: 3: "))
for tip in TipoviPlacanja:
    if tip.value == odabrano:
        print(tip)
        
