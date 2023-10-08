import csv

fajl = open("podaci2.csv")

reader = csv.reader(fajl)

broj_python_smer = 0

for red in reader:
    for podatak in red:
        if podatak.lower(): == "python":
            broj_python_smer += 1
    # print(red[0])
    # for i in range(len(red)):
    

print(broj_python_smer)

            

