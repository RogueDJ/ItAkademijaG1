import http.server as srv
import datetime
import urllib.parse as parse
class Rukovalac(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        parametri = self.path.split("?")[1]
        parametri = dict(parse.parse_qsl(parametri))
        pol = parametri["pol"]
        vreme = datetime.datetime.now()
        izlaz = f"Tacno je{vreme}"
        izlaz += "gospodine" if pol == "m" else "gospodjo"
        self.wfile.write(izlaz.encode())


srv.HTTPServer(("0.0.0.0", 8000), Rukovalac).serve_forever()