kurs = "Python Fundamentals"
print(kurs)
a = 10
b = 5
c = a + b
print(c)
print("Oduzimanje:", a-b)
print("Deljenje:", int(a / b))
print("Celobrojno deljenje:", a // b)
print(10 // 3)
print(10 / 3)
print(a ** 2)

godine = 25
# godine + 1
godine = godine + 1
godine += 1
print(godine)
godine //= 2

# a = input("Unesite prvi broj: ")
# a = int(a)
# b = input("Unesite drugi broj: ")
# b = int(b)
# Rezultat_unosa = (a+b)
# print("Vas rezultat je:", Rezultat_unosa)

# a = int(input("Unesite sumu dinara: "))
# Suma_evra = a * 1.3
# print("Vasa suma evra je:", Suma_evra)
# suma_dolara = a * 1.1


# poluprecnik = float(input("Unesite poluprecnik: "))
# pi = 3.14

# povrsina = poluprecnik ** 2 * pi
# print("Povrsina kruga je:", povrsina)
# a = "5"
# print(a.isnumeric())


# unos = input("Unesi nesto...")
# print(unos.isnumeric())

# stara_kilaza = 77
# nova_kilaza = 85

# print(stara_kilaza > nova_kilaza)
# print(nova_kilaza != 100)

# username = "Test"
# password = "abc1234"

# print(username == "test")
# print(password == "abc1234")

# Broj = int(input("Unesite broj: "))
# provera = Broj % 2

# print(provera == 0)

# korisnik = int(input("Unesite broj: "))
# import random
# moj_broj = random.randint(1,10)
# print("Broj mog kompjuter:", moj_broj)
# print(korisnik == moj_broj)


# automobil                                          cilj
# 0                                                   50

# automobil = 0
# cilj = 50
# print(automobil >= cilj)
# automobil += 10
# print(automobil >= cilj)
# automobil += 10
# print(automobil >= cilj)
# automobil += 10
# print(automobil >= cilj)
# automobil += 10
# print(automobil >= cilj)
# automobil += 10
# print(automobil >= cilj)


# provera_imena = True
# provera_sifre = True
# print(provera_imena and provera_sifre)

kurs = input("Unesite kurs:")
generacija = int(input("Unesite generaciju:"))

odobreno = kurs == "python" and generacija == 2022
print(odobreno)