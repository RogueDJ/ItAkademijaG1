def aleksandra_predaje():
    print("Predavanje....aleksandra lazarevic")

def vladimir_predaje():
    print("Predavanje....vladimir maric")

def predavanje(izlaganje_predavanja):
    print("Pocelo predavanje")
    izlaganje_predavanja()
    print("Zavrseno predavanje!!!")

predavanje(vladimir_predaje)

def levi_klik():
    print("Levi klik misa")

def desni_klik():
    print("Desni klik misa")


def upotreba_aplikacije(klik):
    print("Prikazujem UI")
    print("Izvrsavam interakciju")
    klik()
    print("Nastavljam da koristim program")


upotreba_aplikacije(levi_klik)