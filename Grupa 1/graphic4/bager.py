from drawable import Drawable
import tkinter

class Bager(Drawable):
    def __init__(self, game):
        super().__init__(game)
        self.image = tkinter.PhotoImage(file = "bager2.png")
        self.tage = self.game.canvas.create_image(200,400,image=self.image)
    def update(self,delta):
        pass