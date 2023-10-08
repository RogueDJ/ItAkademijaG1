# ime = input("Unesite ime: ")
# prezime = input("Unesite prezime: ")
# godina = input("Unesite godinu(21, 22, 23...): ")

# korisnicko_ime = ""

# def kreiraj_kor_ime(ime, prezime, godina):
#     kor_ime = f"ita.{godina}.{ime.lower()}.{prezime.lower()}"
#     print("Uspesno kreirano korisnicko ime")
#     return kor_ime

# korisnicko_ime = kreiraj_kor_ime(ime, prezime, godina)
# print(korisnicko_ime)


#funkcija - menjacnica
#parametar - eur
# POVRATNA VREDNOST: rezultat u dinarima

# dinari = int(input("Unesite RSD"))
# def menjacnica(rsd):
#     eur = dinari / 118
#     return eur
# eur = menjacnica(dinari)
# print("Vrednost u evrima je:", round(eur, 2))

# def registracija(licna_karta, cist_automobil, saobracajna):
#     if cist_automobil == False:
#         return "Neuspesno, dodjite opet!"
#     if licna_karta == False:
#         return "Neuspesno, dodjite opet!"
#     if saobracajna == False:
#         return "Neuspesno, dodjite opet!"
    
#     return "Uspesno"

# print(registracija(True, True, False))


# def bankomat(stanje, zeljeni_iznos):
#     if stanje >= zeljeni_iznos:
#         print(f"Uspesno izvrseno. novo stanje je: {stanje - zeljeni_iznos}")
#     else:
#         print(f"Neuspesno, vase stanje je: {stanje}")

# zeljeni_iznos = int(input("Unesite zeljeni iznos: "))
# rezultat = bankomat(3000, zeljeni_iznos)

def registracija(*dokumenti):
    print("Doneli ste dokumenta: ")
    print(dokumenti)

registracija("vozacka dozvola", "obavio tehnicki pregled", "licna karta")

def upis(**podaci):
    print("Uneli ste podatke")
    print(podaci)

upis(ime="Dragan Jovanovic", prezime ="Jovanovic", godiste = 97)


def skolovanje(predavac_predaje):
    print("Skolska godina je u toku...")
    print("Ucionica A22")

    predavac_predaje()

def predavac_vm():
    print("Uvod u mreze")
    print("Danas radimo novu temu")
    print("Da li ste igrali lol")

def predavac_al():
    print("Opet imamo predavanje sredom")
    print("Radimo funkcije")

def predavac_vn():
    print("Krecemo sa kursom HTML i CSS")

skolovanje(predavac_vm)


def priprema_obroka(spremanje):
    print("Dolazak u kuhinju...")
    print("Perem ruke")
    spremanje() 
    

def dorucak():
    print("Idem po burek")








    



