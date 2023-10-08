import http.server as server

class Obrada(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Cao kako je?".encode())

server.HTTPServer(("0.0.0.0",8000),Obrada).serve_forever()