import os

print(os.cpu_count())
os.system("cls")

import sys
print(sys.platform)

import time

# poruka = input("Unesite poruku: ")
# broj_sekundi = int(input("Unesite broj sekundi: "))

# while broj_sekundi > 0:
#     print(f"Preostalo je:{broj_sekundi}")
#     broj_sekundi -= 1
#     time.sleep(1)

# for i in range(10):
#     print(poruka)

print(time.time())

vreme = time.gmtime()
print(vreme.tm_wday)
print(vreme.tm_year)
print(time.ctime())
date = time.localtime()
print(time.strftime("Mesec: %m Godina: %Y Dan: %w", date))

tm = time.localtime


kor = "ita22.python"
novi_kor = kor.replace("22", "23")
print(novi_kor)
prisutni =  "a,b,c,d,b,3d,4r"
prisutni_lista = prisutni.split(",")
print(prisutni_lista)