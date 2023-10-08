import re

sablon = re.compile("kor")
tekst_za_proveru = "korisnicko ime korisnika pocinje sa ita"

if print(sablon.search(tekst_za_proveru)):
    print("nadjeno")
else:
    print("Nema sadrzaja")




sablon = re.compile("[a-zA-Z]")
tekst_za_proveru = "asd_ASD123"
if sablon.search(tekst_za_proveru):
    print("Poseduje slova")
else:
    print("Ne poseduje slova")



sablon = re.compile("^[a-z]{3}[0-9]{2}\.[a-z]+$")
proba = "ita22.proba"
if sablon.match(proba):
    print("Dobro je")
else:
    print("Proverite opet")


