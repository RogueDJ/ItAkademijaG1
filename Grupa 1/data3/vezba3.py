import numpy as np
#godine    = input("Koliko imas godina? ")
#print("Cena karmina je ??????")


godine  = [25,20,30,26,40,38,42,41,39,19]
karmini = [1,1,1,1,0,0,0,0,0,1]

test_x = godine[-2:]
test_y = karmini[-2:]

godine = godine[:-2]
karmini = karmini[:-2]



print(test_x,test_y,godine,karmini)

# for i in range(1000):
#     godine.append(38)
#     karmini.append(0)

print("testiranje: ")

for i in range(2):
    print(f"Test vrednost {test_x[i]}, ocekivano {test_y[i]}")
    nova_musterija = test_x[i]
    ukupno = len(godine)

    x = np.array(godine)
    y = np.array(karmini)

    a = np.sum(y) * np.sum(x**2) 
    a -= (np.sum(x)*np.sum(x*y))
    a /= ((ukupno * np.sum(x**2)) - np.sum(x)**2)

    b = ukupno * np.sum(x*y)
    b -= np.sum(x) * np.sum(y)
    b /= ukupno * np.sum(x**2) - np.sum(x)**2


    predvidjanje = round(a + (b * nova_musterija))

    predvidjanje = round(1 / (1 + np.exp(-predvidjanje)))

    print(f"Dobijeno: {predvidjanje}")



