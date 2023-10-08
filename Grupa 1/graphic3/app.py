import tkinter

class App:
    @staticmethod
    def run():
        print("Aplikacija je startovana")
        app = App()
        app.do_run()

    def promeni(self,naziv):
        if self.current_frame:
            self.current_frame.forget()
        fr = tkinter.Frame(self.win, width=600, height=400,background="yellow")
        fr.pack(fill="both",expand=True)
        self.current_frame = fr

    def do_run(self):
        self.current_frame = None
        self.win = tkinter.Tk()
        self.promeni("blue")
        self.win.mainloop()


App.run()