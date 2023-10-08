class WrongOperation(Exception):
    pass

def Kalkulator(broj1, broj2, operacija):
    dostupne_operacije = ["+","-","*", "/"]
    if operacija not in dostupne_operacije:
        raise WrongOperation
    else:
        if operacija == "+":
            print(broj1+broj2)
        elif operacija == "-":
            print(broj1-broj2)
        elif operacija == "*":
            print(broj1 * broj2)
        elif operacija == "/":
            print(broj1 / broj2)

try:
    Kalkulator(10,5,"?")
except WrongOperation:
    print("Pogresili ste operaciju")
except ZeroDivisionError:
    print("Ne mozete deliti sa 0")
except ValueError:
    print("Pogresna vrednost")
except Exception:
    print("Neka greska")


