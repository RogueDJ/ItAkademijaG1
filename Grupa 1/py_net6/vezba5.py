import http.server as server

proizvodi = {
    "5":"Auto",
    "10":"Telefon"
}

class ObradaZahteva(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parametri = self.path.split("?")[1]

        sadrzaj = "Pozdrav!!!"

        parametri = dict([p.split("=") for p in parametri.split("&") ])
        print(parametri)

        idproizvoda = parametri["id"]



        sadrzaj = open("dovla.html","r").read()

        proizvodi = open("baza.txt", "r").readlines()
        sadrzaj = "Nepostojeci proizvod"
        for p in proizvodi:
            pid,pname = p.split(",")
            if pid == idproizvoda:
                sadrzaj = "Odabrani proizvod: " + pname
                break
            

        sadrzaj = "Odabrani proizvod: " + proizvodi[idproizvoda]

        # sadrzaj = sadrzaj.replace("BOJA", parametri["boja"])
        # sadrzaj = sadrzaj.replace("SLOVA", parametri["slova"])

        self.wfile.write(f"HTTP/1.1 200 Ok\r\nContent-type: text-html\r\nfdsaf: fdsadas\r\nfdsad:odsaiodasj\r\n\r\n{sadrzaj}".encode())
        print("Hello")

s = server.HTTPServer(("0.0.0.0",8000),ObradaZahteva)
s.serve_forever()