# class Karta:
#     def __init__(self, broj, boja, sifra):
#         self.__broj = 0
#         self.__boja = ""
#         self.__sifra = ""
#     @property
#     def broj(self):
#         return self.__broj
#     @property
#     def boja(self):
#         return self.__boja
#     @property
#     def sifra(self):
#         return self.__sifra
    
#     @broj.setter
#     def broj(self, vrednost):
#         self.__broj = vrednost

#     @boja.setter
#     def boja(self, vrednost):
#         self.__boja = vrednost
    
#     @sifra.setter
#     def sifra(self, vrednost):
#         self.__sifra = vrednost

# kartica = Karta()
# print(kartica.broj)
# kartica.broj = 7
# print(kartica.broj)

class Automobil:
    def __init__(self, boja, model):
        self.boja = boja
        self.model = model
        self.__registracija = ""
    @property
    def registracija(self):
        return self.__registracija
    @registracija.setter
    def registracija(self, dokumenta):
        if dokumenta == True:

            self.__registracija = "nasumican broj"

a = Automobil("bela", "ford")
print(a.registracija)
a.registracija = False
print(a.registracija)


