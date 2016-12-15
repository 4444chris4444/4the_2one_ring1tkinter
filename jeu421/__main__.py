from random import seed
from jeu421.partie import Partie
from jeu421.interface import Interface
from tkinter import *

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
        fen1.mainloop()



    def reglement_site():
        print("Pour voir les règlements, simplement aller sur le site http://www.regles-de-jeux.com/regle-du-421/")



    def reglement():
        fen1 = Tk()
        titre = Label(fen1, text="---- RÈGLEMENTS ----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Voir les règlements", command=reglement_site)
        bouton1.grid()
        bouton2 = Button(fen1, text="Ne pas voir les règlements", command=fen1.destroy)
        bouton2.grid()
        fen1.mainloop()

    def page_accueil():
        fen1 = Tk()
        titre = Label(fen1, text="---- MENU ----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Nouvelle partie", command=fen1.destroy)
        bouton1.grid()
        bouton2 = Button(fen1, text="Options")
        bouton2.grid()
        fen1.mainloop()


    x = 2

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



    def ecran_nb_joueur():
        fen1 = Tk()
        titre = Label(fen1, text="---- NOMBRES DE JOUEURS----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="2", command= jouer1)
        bouton1.grid()
        bouton2 = Button(fen1, text="3", command=jouer2)
        bouton2.grid()
        bouton3 = Button(fen1, text="4", command=jouer3)
        bouton3.grid()
        bouton4 = Button(fen1, text="Cliquez sur ce bouton après la sélection du nombre de joueur. Si vous ne sélectionner rien et cliquez sur ce bouton, il y aura automatiquement 2 joueurs.", command=fen1.destroy)
        bouton4.grid()
        fen1.mainloop()

    def ecran_nb_joueur_bot():
        fen1 = Tk()
        titre = Label(fen1, text="---- Voulez-vous jouer contre un ordinateur----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Oui")
        bouton1.grid()
        bouton2 = Button(fen1, text="Non")
        bouton2.grid()
        bouton3 = Button(fen1, text="Cliquez sur ce bouton après la sélection de votre choix. Si vous ne sélectionner rien et cliquez sur ce bouton, il n'y aura pas d'ordinateur.", command=fen1.destroy)
        bouton3.grid()
        fen1.mainloop()

    ecran_nb_joueur()

    ecran_nb_joueur_bot()

    print(x)
    if x==2:
        jeu = Partie(2)
        jeu.jouer()
    if x==3:
        jeu = Partie(3)
        jeu.jouer()
    if x == 4:
        jeu = Partie(4)
        jeu.jouer()


