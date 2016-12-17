from random import seed
from jeu421.partie import Partie
from jeu421.interface import Interface
from tkinter import *
from tkinter import messagebox


if __name__ == "__main__":
    #seed(52) # pour correction ou tests (fixer un seed)
    #interface = Interface()
    #interface.afficher("{}\n*{:^40s}*\n*{:^40s}*\n*{:^40s}*\n{}".format("*"*42, "",
                       #"Bienvenue dans le JEU du 421", "", "*"*42))
    #nombre_joueur = 1
    #while nombre_joueur < 2:
        #nombre_joueur = int(interface.demander_entree("Veuillez saisir un nombre de joueurs (0 pour quitter le jeu): "))
        #if nombre_joueur == 0:
            #break
        #elif not (nombre_joueur >= 2):
            #interface.afficher("Le nombre doit être supérieur ou égale à 2")
        #else:

    def accueil():
        fen1 = Tk()
        titre = Label(fen1, text="---- JEU 421 ----")
        titre.grid(padx=250, pady=250)
        bouton = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()
        fen1.mainloop()

    def reglement():
        fen1 = Tk()
        titre = Label(fen1, text="---- RÈGLEMENTS ----")
        titre.grid(padx=250, pady=250)
        Instruction = Label(fen1, text="Pour voir les règlements, simplement aller sur le site http://www.regles-de-jeux.com/regle-du-421/", font='size, 20')
        Instruction.grid()
        bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton2.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()
        fen1.mainloop()

    def page_accueil():
        fen1 = Tk()
        titre = Label(fen1, text="---- MENU ----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Nouvelle partie", command=fen1.destroy)
        bouton1.grid()
        bouton2 = Button(fen1, text="Options")
        bouton2.grid()
        bouton3 = Button(fen1, text="Quitter",command=exit)
        bouton3.grid()
        fen1.mainloop()


    x = 2
    y = 0

    accueil()

    reglement()


    page_accueil()

    def jouer1():
        global x
        x=2



    def jouer2():
        global x
        x=3

    def jouer3():
        global x
        x=4

    def cpu0():
        global y
        y=0

    def cpu1():
        global y
        y=1


    def combine_funcs(*functions):
        def combined_func(*arg1, **arg2):
            for f in functions:
                f(*arg1, **arg2)

        return combined_func



    def ecran_nb_joueur():
        fen1 = Tk()
        titre = Label(fen1, text="---- NOMBRES DE JOUEURS----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="2", command= combine_funcs(jouer1, fen1.destroy))
        bouton1.grid()
        bouton2 = Button(fen1, text="3", command= combine_funcs(jouer2, fen1.destroy))
        bouton2.grid()
        bouton3 = Button(fen1, text="4", command= combine_funcs(jouer3, fen1.destroy))
        bouton3.grid()
        bouton4 = Button(fen1, text="Quitter", command=exit)
        bouton4.grid()
        fen1.mainloop()

    def ecran_nb_cpu():
        fen1 = Tk()
        titre = Label(fen1, text="---- Voulez-vous jouer contre un ordinateur----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Oui", command= combine_funcs(cpu1, fen1.destroy))
        bouton1.grid()
        bouton2 = Button(fen1, text="Non", command= combine_funcs(cpu0, fen1.destroy))
        bouton2.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()
        fen1.mainloop()

    ecran_nb_joueur()

    ecran_nb_cpu()

    def nb_joueur_nb_bot():
        fen1 = Tk()
        titre = Label(fen1, text="---- Récapitulatif----")
        titre.grid(padx=250, pady=250)
        information=Label(fen1, text="Nombre de joueurs :"+ str(x) + " " + "Avec un ordinateur?" + " " + str(bool(y==1)))
        information.grid()
        bouton1 = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton1.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()
        fen1.mainloop()


    nb_joueur_nb_bot()
try :
    jeu = Partie(x, y)
except NameError :
    print ('valeurs non defini')
    jeu.jouer()


