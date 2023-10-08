import tkinter
import time


prozor = tkinter.Tk()
pos_x = int((prozor.winfo_screenwidth()/2)-400)
pos_y = int((prozor.winfo_screenheight()/2)-300)
prozor.geometry(f"800x600+{pos_x}+{pos_y}")
canvas = tkinter.Canvas(prozor, background='gray')
canvas.pack(fill='both',expand=True)
slike = {
    "desno":tkinter.PhotoImage(file='bager2.png'),
    "levo":tkinter.PhotoImage(file='bager1.png'),
    "pozadina1":tkinter.PhotoImage(file='bgrd.png'),
    "pozadina2":tkinter.PhotoImage(file='bgrd.png')
}
bager = canvas.create_image(200,300,image=slike["desno"])
pozadina1 = canvas.create_image(500,300,image=slike["pozadina1"])
pozadina2 = canvas.create_image(1500,300,image=slike["pozadina2"])
canvas.tag_lower(pozadina1)
canvas.tag_lower(pozadina2)
def bager_click(evt):
    print(evt)

def bager_key(evt):
    kod = evt.keycode
    if kod == 68:
        canvas.itemconfig(bager,image=slike["desno"])
        canvas.move(bager,5,0)
    elif kod == 65:
        canvas.itemconfig(bager,image=slike["levo"])
        canvas.move(bager,-5,0)
    elif kod == 87:
        canvas.move(bager,0,-5)
    elif kod == 83:
        canvas.move(bager,0,5)
    
    print(kod)

canvas.tag_bind(bager,"<Button-1>",bager_click)
prozor.bind("<KeyPress>",bager_key)

zadnje_vreme = time.time()
while True:
    vreme = time.time()
    delta = vreme-zadnje_vreme
    zadnje_vreme = vreme
    x,y = canvas.coords(pozadina1)
    if x <=0:
        canvas.moveto(pozadina1,1500,0)
    x,y = canvas.coords(pozadina2)
    if x <=0:
        canvas.moveto(pozadina2,1500,0)
    canvas.move(pozadina1,-(delta*300),0)
    canvas.move(pozadina2,-(delta*300),0)
    prozor.update()
    time.sleep(0.001)