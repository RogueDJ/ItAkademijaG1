import http.server as server
from urllib import parse

def proveri(uname,pwd):
    fajl = open("users.txt","r")
    while linija := fajl.readline():
        un,pw = linija.lstrip().split(",")
        if un == uname:
            if pwd == pw:
                return 0
            else:
                return -1
    else:
        return -2  

class Hendler(server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        strana = self.path.lstrip("/")
        if not strana or strana == "index.html":
            index_strana = open("index.html","r").read()
            kolacic = self.headers["Cookie"]
            if kolacic:
                ime = kolacic
                index_strana += f"<h3>Dobrodosao {ime}</h3>"
            else:
                index_strana += 'Niste ulogovani, <a href="login.html">ulogujte se</a>'

            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(index_strana.encode())
        else:
            super().do_GET

    def do_POST(self):
        duzina = int(self.headers["Content-Length"])
        podaci = self.rfile.read(duzina).decode()
        podaci = dict(parse.parse_qsl(podaci))
        res = proveri(podaci["username"],podaci["password"])
        if res == 0:
            self.send_response(301)
            self.send_header("Location","index.html")
            self.send_header("Set-Cookie", f"{podaci['username']},;max-age=30")
            self.end_headers()
        elif res == -1:
            self.send_response(200)
            self.send_header("Content-Type","text/html")
            self.end_headers()
            self.wfile.write(b"Nije ispravna lozinka")
            self.wfile.write(b"<br><a href='login.html'>Povratak na login stranu</a>")
        else:
            self.send_response(200)
            self.send_header("Content-Type","text/html")
            self.end_headers()
            self.wfile.write(b"Nepostojeci korisnik")
            self.wfile.write(b"<br><a href='login.html'>Povratak na login stranu</a>")

server.HTTPServer(("0.0.0.0",8000),Hendler).serve_forever()