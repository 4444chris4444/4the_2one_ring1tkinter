from tkinter import Tk, Label, Button

def interface():
    root = Tk()
    titre = Label(root, text="---- JEU 421 ----")
    titre.grid(padx=250, pady=250)
    bouton = Button(root, text="Continuer")
    bouton.grid()

    root.mainloop()


interface()