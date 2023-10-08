print("Cao")
print("Danasnji datum je 2.12")
print("Predavanje python")

ime = "Sofija"
len(ime)
ime.upper()

def ispisi_poruke():
    print("Cao")
    print("Danasnji datum je 2.12")
    print("Predavanje python")

ispisi_poruke()


def pozdravna_poruka(ime):
    print(f"Hello {ime}")
pozdravna_poruka("Sofija")

def prikazi_informacija(ime ="", poeni = 0):
    print(f"Student: {ime}, poeni: {poeni}")

prikazi_informacija("Sofija", 98)


def saberi(a, b):
    print(a+b)
saberi(8,10)
saberi(a = 10, b = 9)

def kalkulator(a, b, o):
    if o == "+":
        print(a+b)
        return a + b
    elif o == "-":
        print(a-b)
        return a - b
    elif o == "*":
        print(a * b)
        return a * b
    elif o == "/":
        if a == 0 or b == 0:
            print("Nije dozvoljeno deljenje sa nulom")
        else:
            print(a/b)
            return a / b

# kalkulator(int(input("Unesite prvi broj:")), int(input("Unesite drugi broj:")), input("Unesite operaciju(+, -, *, /):"))


def info_o_automobilima(automobili):
    pass



lista = ["a", "b", "c"]

broj_clanova = len(lista)

