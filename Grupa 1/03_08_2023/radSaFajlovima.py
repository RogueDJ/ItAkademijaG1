import os
fajl = open("podaci1.txt", "w+")
sadrzaj_fajla = fajl.read()
print(sadrzaj_fajla)

fajl.write("\nproba")

fajl.close()
os.unlink("podaci1.txt")
