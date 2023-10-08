import time
import socket
class Heroj:

    def __init__(self):
        self.health = 100
        self.slusaci_promena_healtha = []

    def hit(self,dmg):
        self.health -= dmg
        for slusac_promene_healtha in self.slusaci_promena_healtha:

            slusac_promene_healtha(self.health)

def hud(health):
    print(f"Izmena na health-u({health})")

def mreza(health):
    s = socket.socket()
    s.connect(("127.0.0.1",8000))
    s.send(f"Slanje hp za heroja, preko mreze({health})".encode())
    s.close()

def displej(health):
    print(f"Prikaz izmene health-a na displeju({health})")


wind = Heroj()
wind.slusaci_promena_healtha.append(hud)
wind.slusaci_promena_healtha.append(mreza)
wind.slusaci_promena_healtha.append(displej)
for i in range(10):
    wind.hit(5)
    
