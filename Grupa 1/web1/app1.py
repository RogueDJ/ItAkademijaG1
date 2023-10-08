import http.server as srv
import datetime
import urllib.parse as parse

model = {
    "1":{
        "naziv":"Fender Stratocaster YJM WH",
        "slika":"fender.jpg",
        "cena": 2300
    },
    "5":{
        "naziv":"Ibanez Jem",
        "slika":"https://images.guitarguitar.co.uk/cdn/large/130/14123111035558f.jpg?h=500&maxwidth=770&scale=canvas&bg=ffffff&quality=70",
        "cena": 500
    },
    "12":{
        "naziv":"Paul Standard",
        "slika":"https://www.mitrosmusic.com/media/inlineimage/upload_44617_1_d.jpg",
        "cena": 2800
    }
}

class Rukovalac(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        if self.path.startswith("/admin"):
            self.wfile.write(open("admin.html","rb").read())
            return 

        parametri = self.path.split("?")
        izlaz = ""
        if len(parametri) > 1: 
            parametri = dict(parse.parse_qsl(parametri[1]))
            pid = parametri["id"]
            gitara = model[pid]
            izlaz = f"<h3>{gitara['naziv']}</h3><img width=200 src='{gitara['slika']}'/><br><strong>Cena: </strong>{gitara['cena']}<br><br><a href='/'>Nazad</a>"
        else:
            for kljuc, vrednost in model.items():
                izlaz += f"<a href='?id={kljuc}'>{vrednost['naziv']}</a><br>"
        
     
        self.wfile.write(izlaz.encode())

    def do_POST(self):
        duzina = int(self.headers["Content-Length"])
        telo = self.rfile.read(duzina).decode()
        parametri = dict(parse.parse_qsl(telo))
        novi_id = 1
        for i in model:
            novi_id = str(int(i)+1)
        model[novi_id] = parametri
        self.send_response(301)
        self.send_header("Location", "/")
        self.end_headers()

        print(novi_id, parametri)


srv.HTTPServer(("0.0.0.0", 8000), Rukovalac).serve_forever()