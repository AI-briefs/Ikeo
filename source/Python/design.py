from tkinter import Tk, Frame, Label, IntVar, Checkbutton, Button, Toplevel, ttk
from query import Query


class Graphique:

    def __init__(self):
        self.window = Tk()
        self.window.title("Ikeo")
        self.window.geometry("720x480")
        self.window.config(background='#41B77F')
        self.values = Query().get_produit_usine()
        

        self.display_produit_usine()

    def display_produit_usine(self):
        i = 0
        for j,k in self.values.items():
            frameLeft = Frame(self.window).grid(row=i, column=i)
            frameRight = Frame(self.window).grid(row=i, column=i)

            label = Label(frameLeft, text=j).grid(row=i, column=0)
            label = Label(frameRight, text=k).grid(row=i, column=1)
            i+=1

app = Graphique()
app.window.mainloop()