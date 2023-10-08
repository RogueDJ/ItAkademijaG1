import urllib.parse 
def parsiraj_putanju(putanja): 
    # putanja                 = "/dovla/ricma?a=2&b=3"
    putanja                 = putanja.lstrip("/") #shop/products
    putanja_i_parametri     = putanja.split("?")
    putanja                 = putanja_i_parametri[0]
    putanja_delovi          = putanja.split("/") # ['shop','products']

    broj_delova_putanja     = len(putanja_delovi)

    kontroler               = "mojkontroler"
    funkcionalnost          = "index"

    if broj_delova_putanja == 2:    
        kontroler               = putanja_delovi[0]
        funkcionalnost          = putanja_delovi[1]
    elif broj_delova_putanja == 1 and putanja_delovi[0]:
        kontroler               = putanja_delovi[0]

    parametri = {}
    if len(putanja_i_parametri) == 2:
        parametri = dict(urllib.parse.parse_qsl(putanja_i_parametri[1]))

    return kontroler,funkcionalnost,parametri
