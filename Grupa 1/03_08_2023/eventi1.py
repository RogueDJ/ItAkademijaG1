def rezervoar_lampica():
    print("Na rezervi ste")
    print("Zuta lampica")

def rezervoar_lampica2():
    print("Na rezervi ste, pozurite")
    print("Crvena lampica")
import time
def vozi(gorivo, indikator_goriva):
    rezerva_limit = 10
    while gorivo > 0:
        print(f"Voznja, Stanje goriva je:{gorivo}")
        time.sleep(1)
        gorivo -= 5
        if gorivo <= rezerva_limit:
            indikator_goriva()


vozi(40, rezervoar_lampica2)