import csv
fajl = open("vezba.csv")
reader = csv.reader(fajl)
username = input("Unesite korisnicko ime: ")
password = input("Unesite sifru: ")
for red in reader:
    if username == red[0] and password == red[1]:
        print(f"Stanje: {red[2]}")