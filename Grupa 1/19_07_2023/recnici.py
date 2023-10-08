# Osoba = ["Sofija", 25, True]
# print(Osoba[0])
# osoba_recnik = {"ime": "Sofija", "godine": 25, "zauzeta": True}
# print(osoba_recnik)
# print(osoba_recnik["ime"])

# for i in osoba_recnik:
#     print(osoba_recnik[i])
# for (kljuc, vrednost) in osoba_recnik.items():
#     print("Ovo je kjuc:", kljuc)
#     print("Ovo je vrednost:", vrednost)

# osoba2 = {}

# osoba2["ime"] = "Marija"
# print(osoba2)

# osoba2["ime"] = "Sofija"
# print(osoba2)

# del osoba2["ime"]
# print(osoba2)

# poruke = {"en": "Hello", "sr": "Zdravo", "de": "Hallo"}

# # jezik = input("Unesite jezik: ")
# # if jezik == "en" or "sr" or "de":
# #     print(poruke[jezik])
# # else:
# #     print("Nemamo ovaj prevod")

# for(jezik, prevod) in poruke:
#     if jezik == "en":
#         print(f"ENGLESKI:{prevod}")
#     elif jezik == "sr":
#         print(f"SRPSKI: {prevod}")
#     else:
#         print(f"NEMACKI")           



# selekcija = {
#     "drzava": "Srbija",
#     "broj pobeda": "0",
#     "boje dresova": ["crvena", "bela"],
#     "brojevi igraca": [9, 5, 13, 20]
#                    }

# for (kljuc, vrednost) in selekcija.items():
#     print("KLJUC:", kljuc)
#     print("VREDNOST:", vrednost)
#     if kljuc == "boje dresova":
#         for boja in vrednost:
#             print("Boja:", boja)
#     elif kljuc == "brojevi igraca": 
#         for broj in vrednost:
#             print("Igrac broj:", broj)
#     else:
#         print(f"{kljuc.capitalize()}: {vrednost}")    

# ime = "Sofija"
# godine = 25
# plava = True
# slobodna = False

# print("Devojka", ime, "ima", godine, "godina i kosu koja je")

# opis_devojke = f"Ime {ime} je {slobodna} i ima {godine} godina"
# print(opis_devojke)


automobil = {
"Marka": "Citroen",
"Model": "C3",
"boje": ["Crvena", "Bela", "crna"],
"Alu felne": False,
"godiste": "2017",
"kubikaza": 1.6
}

for kljuc, vrednost in automobil.items():
    if kljuc == "Marka":
        print(f"{kljuc}: {vrednost}")
    elif kljuc == "Model":
        print(f"{kljuc}: {vrednost}")
    elif kljuc == "boje":
        for boja in vrednost:
            print("Boja: ", boja)
    elif kljuc == "Alu felne" and vrednost == False:
        print("Nema alu felne...")
    elif kljuc == "kubikaza":
        print("Snaga motora je:", vrednost)


automobili = {
    "BG-123": {
        "model": "Citroen",
        "model": "C3",
        "kubikaza": 1.6,
        "boje": ["crvena", "bela", "crna"]
    },
    "BG-279": {
        "model": "Opel",
        "marka": "Astra",
        "kubikaza": 2.0,
        "boje": ["plava", "metalik"]
    },
    "BG-287": {
        "model": "Audi",
        "marka": "A2",
        "kubikaza": 2.4,
        "boje": ["crna", "bela"]  
    }
}
for reg, detalji in automobili.items():    
    for kljuc, vrednost in detalji.items():
        print(f"{kljuc}: {vrednost}")
    print("----------------------------------")


kursevi = {
    "PPF": {
        "naziv": "Python Fundamentals",
        "semestar": 1
    },
     "POO": {
         "naziv": "Python Object Oriented",
         "semestar": 1
    }
}
for id_kursa, detalji in kursevi.items():
    for k, v in detalji.items():
        print(k, v)



    
        
        

