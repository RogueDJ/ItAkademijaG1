import requests
from bs4 import BeautifulSoup
from bs4 import ResultSet
from bs4.element import Tag
import mysql.connector as con
tekst = requests.get("https://www.it-akademija.com/utisci-iskustva-uspesi-nasih-polaznika").text

dokument = BeautifulSoup(tekst,features='html.parser')

divovi = dokument.find_all("div")
# t=Tag()
# t.get

divovi = [div for div in divovi if'class' in div.attrs and div['class'][0] =='oIti']
total = 0
db = con.connect(host='localhost',database='statistika',user='root', passwd='')
cur = db.cursor()
for polaznik in divovi:
    imaposao = "posao" in polaznik.text
    naslov =polaznik.find("h2").text
    imeiprezime = polaznik.find_all("p")
    if len(imeiprezime)<1:
        continue
    imeiprezime = imeiprezime[len(imeiprezime)-1]
    if not imeiprezime:
        continue
    imeiprezime = imeiprezime.find("strong")
    if not imeiprezime:
        continue
    imeiprezime = imeiprezime.text
    imeiprezime = imeiprezime.split(",")[0].strip()
    print(naslov)
    print(imeiprezime)
    print(imaposao)
    total += imaposao == True
    cur.execute(f"insert into polaznici values(null,%s,%s,%s)",[imeiprezime,naslov,imaposao])
db.commit()
print(total)
    


'''
<div class="oIti">
<h2>ITAcademy mi je jak oslonac za karijeru i napredak</h2>
<p><img src="https://www.it-akademija.com/cms/mestoZaUploadFajlove/boskomil.png" width="85" height="90" border="0" align="left" />ITAcademy sam upisao zato &scaron;to je to bila jedina obrazovna ustanova koja je nudila detaljniju edukaciju iz JAVA programskog jezika, &scaron;to je bilo i vi&scaron;e nego dovoljno da se opredelim istu.<br /><br />&Scaron;kolovanje je bilo mnogo zanimljivije od uobičajenog, jer sam svoju &bdquo;&scaron;kolu&ldquo; mogao poneti sa sobom, gde god bih imao pristup internetu. Profesori su mi uvek bili na raspolaganju ukoliko bih se susreo sa određenim nedoumicama i nije bilo potrebe da odlazim na konsultacije i predavanja, čime sam u&scaron;tedeo mnogo na vremenu kojeg nisam imao na pretek, jer sam bio zaposlen.<br /><br />ITAcademy mi je poslužila kao jak oslonac za dalju karijeru i napredak, jer znanje koje sam ovde stekao, stavilo me za korak ispred ljudi koji su aplicirali za posao JAVA Developera. Dovoljno je bilo da kompanije vide nastavni plan i program JAVA Developmenta koji sam dostavio u propratnom pismu. Nastavio sam sa usavr&scaron;avanjem u oblasti smera koji sam zavr&scaron;io, sve zahvaljujući kvalitetnom upoznavanju sa osnovama.</p>
<p><strong>Bo&scaron;ko Velisavljević </strong></p>
</div>
'''

