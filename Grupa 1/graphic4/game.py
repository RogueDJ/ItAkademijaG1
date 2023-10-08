import tkinter
import time

class Game:
    def __init__(self):
        self.game_objects = []
        self.keys = {}
        self.prozor = tkinter.Tk()
        pos_x = int((self.prozor.winfo_screenwidth()/2)-400)
        pos_y = int((self.prozor.winfo_screenheight()/2)-300)
        self.prozor.geometry(f"800x600+{pos_x}+{pos_y}")
        self.canvas = tkinter.Canvas(self.prozor, background='gray')
        self.canvas.pack(fill='both',expand=True)
        self.zadnje_vreme = time.time()
        self.prozor.bind("<KeyPress>",self.keydown)
        self.prozor.bind("<KeyRelease>",self.keyup)

    def keyup(self,evt):
        del self.keys[evt.keycode]
    def keydown(self,evt):
        self.keys[evt.keycode] = True


    def start(self):
        while True:
            vreme = time.time()
            delta = vreme-self.zadnje_vreme
            self.zadnje_vreme = vreme
            for game_object in self.game_objects:
                game_object.update(delta)
            self.prozor.update()
            time.sleep(0.001)