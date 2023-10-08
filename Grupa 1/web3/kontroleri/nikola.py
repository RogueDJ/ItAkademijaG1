import model
def index(param={}):
    a = int(param["a"])
    b = int(param["b"])
    return f"Rezultat {a+b}"

def proba(param={}):
    izlaz = ""
    karakteri = model.svipodaci()
    for k,v in karakteri.items():
        izlaz += f"<a href='/nikola/detalji?id={k}'><div style='background-color:red;padding:4px;margin:4px;color:white;'>{v['ime']}</div></a>"
    return izlaz

def detalji(param={}):
    karakter = model.podatak(param["id"])
    izlaz = "Podaci o karakteru su: <br>"
    izlaz += f"Ime:{karakter['ime']}<br>"
    izlaz += f"Popularnost: {karakter['popularnost']}<br>"
    izlaz += f"<img src='{karakter['slika']}' width=200 /><br>"
    izlaz += "<a href='/nikola/proba'>Povratak na listu karaktera</a>"
    return izlaz