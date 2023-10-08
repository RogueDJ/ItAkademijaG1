class Proizvod:
    def __init__(self, naziv, opis, cena):
        self.naziv = naziv
        self.opis = opis
        self.cena = cena

class Korpa:
    def __init__(self, spisak_proizvoda):
        self.spisak_proizvoda = spisak_proizvoda
        res = 0
        for pr in spisak_proizvoda:
            res += pr.cena
        self.ukupna_cena = res

pr1 = Proizvod("Patike", "fudbalske", 5000)
pr2 = Proizvod("Patike", "Kosarkaske", 10000)
pr3 = Proizvod("Papuce", "Crocs", 3000)

lista_pr = []
lista_pr.append(pr2)
lista_pr.append(pr1)

korpa = Korpa(lista_pr)
print(korpa.ukupna_cena)