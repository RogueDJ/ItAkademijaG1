import tkinter

prozor = tkinter.Tk()
lbl_proizvod = tkinter.Label(prozor)
lbl_proizvod.config({"text":"Krcenje"})
lbl_proizvod["background"] = "blue"
lbl_proizvod["foreground"] = "white"
lbl_proizvod["font"] =("Arial",24)
lbl_proizvod["pady"] = 10
lbl_proizvod.pack()
lbl_proizvod.pack_configure({"fill":"x"})
lbl_proizvod["anchor"] = "e"

lbl_cena = tkinter.Label(prozor,text="400e",font=("Arial",24),anchor="w")
lbl_cena.pack(fill="x")
lbl_trava = tkinter.Label(prozor,background="green",bitmap="question")
lbl_trava.pack()
prozor.mainloop()