import pandas,random

v1 = pandas.Series(["Trbusnjaci",60,1])
v2 = pandas.Series(["Sklekovi",30,1])
v3 = pandas.Series(["Burpi",20,2])

podaci = [
    ["Trbusnjaci",60,1],
    ["Sklekovi",30,1],
    ["Burpi",20,2],
    ["Trcanje" , 20 , 2]
]

tabela = pandas.DataFrame(podaci, columns=["naziv","trajanje","tip"])

vezba = ["Zgibovi",5,1]
tabela1 = pandas.DataFrame([vezba],columns=["naziv","trajanje","tip"])
tabela = pandas.concat([tabela,tabela1],ignore_index=True)
print(tabela)

