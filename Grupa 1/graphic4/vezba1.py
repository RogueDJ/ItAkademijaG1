import tkinter


prozor = tkinter.Tk()
pos_x = int((prozor.winfo_screenwidth()/2)-400)
pos_y = int((prozor.winfo_screenheight()/2)-300)
prozor.geometry(f"800x600+{pos_x}+{pos_y}")

canvas = tkinter.Canvas(prozor, background='gray')

canvas.pack(fill='both',expand=True)
canvas.create_rectangle(10,10,110,110, fill ="red",width=3,outline='blue',tags="crtezi")
canvas.create_oval(200,200,100,100,fill='green',width=3,outline='yellow',tags="crtezi")
canvas.create_text(200,200,text='Dovla je najlepsi predavac',font=('Arial',24),fill='red',tags="crtezi")
slika = tkinter.PhotoImage(file='bager1.png')
bager = canvas.create_image(300,300,image=slika)
slika1=tkinter.PhotoImage(file='bgrd.png')
pozadina = canvas.create_image(500,300,image=slika1)
canvas.tag_lower(pozadina)
canvas.move(pozadina,-100,0)
canvas.moveto("crtezi",300,300)
print(pozadina)

def bager_click(evt):
    print(evt)

canvas.tag_bind(bager,"<Button-1>",bager_click)


prozor.mainloop()