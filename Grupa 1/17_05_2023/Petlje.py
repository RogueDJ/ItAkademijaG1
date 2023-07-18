# x ........................... cilj
pozicija_automobila = 0
pozicija_cilja = 10
pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

for ime in ["Marko", "Milos", "Sofija", "Desport", "Nevena"]:
    print("Hello", ime)

print("Prva sledeca linija....")


for broj in [1, 2, 3, 4, 5, 6, 7]:
    print("Ovo je broj:", broj)

for broj in range(1, 21):
    print("Stampanje broja:", broj)

for broj in range(100, 0, -1):
    print("Prikaz:", broj)



pozicija_automobila = 0
pozicija_cilja = 10
for kretanja in range(5):
    pozicija_automobila += 2
    print(pozicija_automobila == pozicija_cilja)

start_date = 2010
end_date = 2015
for datum in range(start_date, end_date + 1):
    print(datum)

for zvezda in range(100):
    print("*", end = "")
print()
# print("1\t2\t3")
# print ("****************")
# zeljeni_broj = int(int("Unesite broj: "))

# # for brojac in range(1, zeljeni_broj + 1):
# #     print(brojac * 1, end = "\t")
# #     print(brojac * 2, end = "\t")
# #     print(brojac * 3)


#n za novi red, t za razmak u istom redu


# for x in range(5):
#     for y in range(3):
#         print("Ovo je x:", x, "Ovo je y:", y)


for x in range(6):
    for y in range(6):
        if x == y:
            print("#", end = "")
        else:
            print("*", end = "")
        # print("*" if x == y else "#", end = "")
    print()

for w in range(10):
    for h in range(10):
        if w == 0 or w == 9 or h == 0 or h == 9:
            print("#", end = "")
        else:
            print(" ", end = "")
    print()
   



        



