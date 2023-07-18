# brojevi = [9, 1, 3, 2, 5, 8, 7]

# brojevi.sort()
# brojevi.reverse()
# print(brojevi)

# brojevi = [9, 1, 3, 2, 5, 8, 7]

# sortirani_brojevi = [1, 2, 3, 5, 7, 8, 9]
# while True:
#     izvrsena_zamena = False
#     for i in range(1, len(brojevi)):
#         if brojevi[i] < brojevi[i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break

# print(brojevi)
        
# Proizvodi = ["Telefon", "TV", "Kompjuter"]   
# Cene = [155.95, 189.35, 800.32] 
# for i in range(len(Proizvodi)):
#     print(Proizvodi[i], Cene[i])

# automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peugeot"]
# for i in range(len(automobili)):
#     if i == 3:      
#         print("Ovo Aleksandar vozi:", automobili[i])

# proizvodi = [
#     ["iphone 11", "Samsung s22", "xiaomi x3"],
#     ["acer", "macbook", "dell"],
#     ["ipad", "galaxy tab", "xiaomi tablet"]
#             ]
# telefoni = ["iphone 11", "Samsung s22", "xiaomi x3"]
# laptopovi = ["acer", "macbook", "dell"]
# tableti = ["ipad", "galaxy tab", "xiaomi tablet"]

# print(proizvodi[0][0])
# # proizvodi = [telefoni, laptopovi, tableti]

# for i in range(len(proizvodi)):
#     print(proizvodi[i])
#     for j in range(len(proizvodi[i])):
#         print (proizvodi[i][j])

# hrana = [
#     ["cokolada", "bombone", "palacinke"],
#     ["sarma", "musaka","kiseli kupus"],
#     ["pecena paprika", "ajvar","sopska"]
# ]
# for kategorija in hrana:
#     for jelo in kategorija: 
#         print("Naziv:", jelo)

# ime = "Sofija"
# poruka = f"Cao {ime}!!!"
# print(poruka)

# a = 10
# b = 15
# sabiranje = f"Sabiranje brojeva {a} i {b} je {a+b}"
# print(sabiranje)

biblioteka =            [
    ["neki naslov", "autor2", 432],
    ["drugi naslov", "blad1", 129]         
]
while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            print(knjiga)
    if komanda == 3:
        kljucna_rec = input("Unesite naziv koji zelite da obrisete. ")
        for knjiga in biblioteka:
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")

    if komanda > 3:
        break


