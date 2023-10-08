# brojevi = [1,3,5]
# try:
#     print(brojevi[6])
#     print("Ispisan je broj")
# except:
#     print("Doslo je do neke greske")

# print("Nastavak programa")
# print("Kraj programa")

# try:
#     broj1 = int(input("Unesite prvi broj: "))
#     broj2 = int(input("Unesite drugi broj: ")) 
#     print("Deljenje")
#     print(broj1/broj2)
#     print("Rezultat je:", broj1/broj2)
# except ZeroDivisionError as greska1:
#     print(greska1)
#     print("Doslo je do greske, pokusajte ponovo")
# except ValueError as greska2:
#     print(greska2)
#     print("Ne mozete uneti tekst u broj")
# except Exception as greska3:
#     print(greska3)
#     print("Izgleda da je neka druga greska")

def sabiranje(a, b):
    if a > 5:
        print(a/b)
    else:
        raise Exception("Broj mora biti veci od pet")
    
try:
    sabiranje(7,0)
except Exception as ex:
    print(ex)
    



