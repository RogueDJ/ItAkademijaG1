class Osoba:
    ime = ""
    prezime = ""
    godine = 0

osoba1 = Osoba()
print(osoba1.godine)
osoba1.ime = "Sofija"
osoba1.prezime = "Malek"
osoba1.godine = 25

print(osoba1.ime, osoba1.prezime, osoba1.godine)


osoba2 = Osoba()
osoba2.ime = "Cokoladna"
osoba2.prezime = "Dorina"
osoba2.godine = 30

print(osoba2.ime)

prisutna = [osoba1, osoba2]

for o in prisutna:
    print (f"Ime:{o.ime}")
    print(f"Prezime:{o.prezime}")