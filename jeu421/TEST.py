from tkinter import *

def accueil():
    fen1 = Tk()
    titre = Label(fen1, text="---- JEU 421 ----")
    titre.grid(padx=250, pady=250)
    bouton = Button(fen1, text="Continuer", command= fen1.destroy)
    bouton.grid()
    fen1.mainloop()

accueil()
