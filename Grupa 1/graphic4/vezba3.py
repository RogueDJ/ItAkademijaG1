from drawable import Drawable
from game import Game
from bager import Bager

g = Game()
bager = Bager(g)
g.game_objects.append(bager)

g.start()