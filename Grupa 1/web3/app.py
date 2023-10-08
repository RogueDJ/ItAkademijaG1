import http.server as server
import pomoc
import importlib

class Hendler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        modul,funkcija,p = pomoc.parsiraj_putanju(self.path)
        m = importlib.import_module(f"kontroleri.{modul}")

        f = getattr(m,funkcija)
        izlaz = f(p)
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.end_headers()
        self.wfile.write(izlaz.encode())
server.HTTPServer(("0.0.0.0",8000),Hendler).serve_forever()