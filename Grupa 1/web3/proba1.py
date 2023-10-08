import pomoc

from string import Template

tekst = "<h3>[ime] je najjaci predavac</h3>"

sablon = Template(tekst)

tekst = tekst.replace('[ime]', 'dovla ricma')
tekst = sablon.substitute({"ime":"Dovla Ricma"})
print(tekst)