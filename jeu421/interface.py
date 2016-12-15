from tkinter import *

class Interface:
    def __init__(self):
        pass

    def choisir_des_a_relancer(self, resultat_du_lancer):
        """
        Méthode permettant de choisir selon un résultat de lancé de dés les dés qu'il veut relancer.
        Dans cette méthode, doit demander à l'utilisateur les valeurs de dés à relancer.
        Tant que les valeurs entrées ne sont pas dans la liste en paramètre, vous devez le redemander au joueur.
        :param resultat_du_lancer:  la liste des valeurs des dés où il faut choisir les valeurs de dés  à relancer
        :return: la liste des valeurs des dés choisis pour le relancement
        """
        n = len(resultat_du_lancer)
        choisir = True
        while choisir:
            choisir = False
            resultat_du_lancer_copie = resultat_du_lancer[:]
            temp = input("Choississez les dés à relancer. Exemple: 24 pour relancer les dés de valeurs 2 et 4\n"
                         "(Laissez vide pour garder votre combinaison actuelle):")
            temp = list(map(int, list(temp)))
            if len(temp) > n:
                choisir = True
            else:
                for v in temp:
                    if v in resultat_du_lancer_copie:
                        resultat_du_lancer_copie.remove(v)
                    else:
                        choisir = True
                        break
            if choisir:
                print("Trop de valeurs ou un des dés à relancer est invalide!")
        return temp

    def demander_entree(self, message_demande=""):
        return input(message_demande)

    def afficher(self, message=""):
        print(message)

    @staticmethod
    def accueil():
        fen1 = Tk()
        titre = Label(fen1, text="---- JEU 421 ----")
        titre.grid(padx=250, pady=250)
        bouton = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton.grid()
        fen1.mainloop()

    @staticmethod
    def reglement_site():
        print("Pour voir les règlements, simplement aller sur le site http://www.regles-de-jeux.com/regle-du-421/")

    @staticmethod
    def reglement():
        fen1 = Tk()
        titre = Label(fen1, text="---- RÈGLEMENTS ----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Voir les règlements", command=reglement_site)
        bouton1.grid()
        bouton2 = Button(fen1, text="Ne pas voir les règlements", command=fen1.destroy)
        bouton2.grid()
        fen1.mainloop()

    @staticmethod
    def reglement():
        fen1 = Tk()
        titre = Label(fen1, text="---- RÈGLEMENTS ----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Voir les règlements", command=print(
            "Pour voir les règlements, simplement aller sur le site http://www.regles-de-jeux.com/regle-du-421/"))
        bouton1.grid()
        bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton2.grid()
        fen1.mainloop()

    @staticmethod
    def page_accueil():
        fen1 = Tk()
        titre = Label(fen1, text="---- MENU ----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Nouvelle partie", command=fen1.destroy)
        bouton1.grid()
        bouton2 = Button(fen1, text="Options")
        bouton2.grid()
        fen1.mainloop()