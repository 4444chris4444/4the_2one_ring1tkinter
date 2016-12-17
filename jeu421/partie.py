from jeu421.interface import Interface
from jeu421.combinaison import *
from jeu421.joueur import Joueur
from jeu421.joueur import JoueurAlgo
from tkinter import *
import os


class Partie:
    """
    Classe représentant une partie de 421. Une partie a les attributs suivants:
    - nb_joueurs: le nombre de joueurs dans la partie
    - joueurs: la liste des joueurs de la partie
    - nb_jetons_du_pot: le nombre de jetons dans le pot de la partie
    - nb_maximum_lancer: le nombre maximum de lancés permis pendant la décharge
    - premier: l'indice du premier joueur pour le tour courant, donc change possiblement
    """
    interface = Interface()

    def __init__(self, nb_joueurs, nb_cpu):
        """
        Constructeur de la classe. Vous devez initialisez les attributs
        :param nb_joueurs: le nombre de joueur de la partie
        """
        assert nb_joueurs >= 2, "Il faut au moins deux joueurs pour une partie de 421"
        self.nb_cpu = nb_cpu
        self.nb_joueurs = nb_joueurs
        self.nb_total_joueurs = nb_cpu + nb_joueurs
        if nb_cpu == 0:
            self.joueurs = [Joueur("Joueur{}".format(i+1)) for i in range(nb_joueurs)]
        else:
            self.joueurs = [Joueur("Joueur{}".format(i + 1)) for i in range(nb_joueurs)]
            self.joueurs.append((Joueur("Ordinateur")))
        self.nb_jetons_du_pot = NOMBRE_DE_JETONS_DU_JEU
        self.premier = 0


    def determiner_premier_lanceur(self):
        """
        Cette méthode permet de déterminer le premier joueur qui lancera dans la partie.
        Tous les joueurs sont sensé lancer un dé et c'est celui qui a le plus petit nombre qui jouera plus tard le
        premier tour.
        En cas d'égalité, les joueurs concernés répètent l'opération
        L'attribut premier de la classe est initialisé à l'appel de cette méthode
        :return:
        """
        fen1 = Tk()
        titre = Label(fen1, text="---- Détermination du premier joueur----")
        titre.grid(padx=250, pady=250)
        bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton2.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()
        fen1.mainloop()
        #Partie.interface.afficher("*{:^40s}*".format("Détermination du premier joueur"))
        concernes = list(range(self.nb_total_joueurs))
        while len(concernes) > 1:
            best_valeur = 7
            premiers = []
            for i in concernes:
                fen1 = Tk()
                titre = Label(fen1, text="Tour de {}".format(self.joueurs[i].nom))
                titre.grid(padx=250, pady=250)
                bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
                bouton2.grid()
                bouton3 = Button(fen1, text="Quitter", command=exit)
                bouton3.grid()
                fen1.mainloop()
                fen1 = Tk()
                titre = Label(fen1, text="Préparez-vous à lancer les dés")
                titre.grid(padx=250, pady=250)
                bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
                bouton2.grid()
                bouton3 = Button(fen1, text="Quitter", command=exit)
                bouton3.grid()
                fen1.mainloop()
                #Partie.interface.demander_entree("Tour de {}: Appuyer sur la touche"
                                                 #" Enter pour lancer!".format(self.joueurs[i].nom))
                valeur = self.joueurs[i].lancer_des(1)[0]
                fen1 = Tk()
                titre = Label(fen1, text="Résultat du lancer:{}\n".format(valeur))
                titre.grid(padx=250, pady=250)
                bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
                bouton2.grid()
                bouton3 = Button(fen1, text="Quitter", command=exit)
                bouton3.grid()
                fen1.mainloop()
                #Partie.interface.afficher("Résultat du lancer:{}\n".format(valeur))
                if valeur < best_valeur:
                    best_valeur = valeur
                    premiers = [i]
                elif valeur == best_valeur:
                    premiers += [i]

            concernes = premiers
            if len(concernes) > 1:
                fen1 = Tk()
                titre = Label(fen1, text="Égalité entre les joueurs: {}".format(", ".join([str(i+1) for i in concernes])))
                titre.grid(padx=250, pady=250)
                bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
                bouton2.grid()
                bouton3 = Button(fen1, text="Quitter", command=exit)
                bouton3.grid()
                fen1.mainloop()
                #Partie.interface.afficher("Égalité entre les joueurs: {}".format(", ".join([str(i+1) for i in concernes])))
        self.premier = concernes[0]
        fen1 = Tk()
        titre = Label(fen1, text="{} sera le premier lanceur\n".format(self.joueurs[self.premier].nom))
        titre.grid(padx=250, pady=250)
        bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton2.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()
        fen1.mainloop()
        #Partie.interface.afficher("{} sera le premier lanceur\n".format(self.joueurs[self.premier].nom))

    def jouer_tour_premiere_phase(self):
        """
        Cette méthode permet de faire le tour de tous les joueurs et leur permet de jouer pendant la charge.
        Rappel: pendant la charge chaque joueur ne peut lancer les dés qu'une seule fois et le perdant du tour doit
        prendre dans le pot un nombre de jetons égale au nombre de points du gagnant du tour.
        Vous devez afficher à l'interface un récapitulatif des jetons des joueurs après chaque tour
        :return: un tuple d'entier qui correspond à l'index du perdant et celui du gagnant du tour
        """
        nb_maximum_lancer = 1
        for i in range(self.nb_total_joueurs):
            pos = (self.premier+i) % self.nb_total_joueurs
            fen1 = Tk()
            titre = Label(fen1,text="Tour du {}".format(self.joueurs[pos].nom))
            titre.grid(padx=250, pady=250)
            bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
            bouton2.grid()
            bouton3 = Button(fen1, text="Quitter", command=exit)
            bouton3.grid()
            fen1.mainloop()
            #Partie.interface.afficher("Tour du {}".format(self.joueurs[pos].nom))
            self.joueurs[pos].jouer_tour(nb_maximum_lancer=nb_maximum_lancer)

            # Si le joueur a pigé une nénette, il doit prendre deux jetons dans le pot
            if self.joueurs[pos].combinaison_actuelle.est_nenette():
                fen1 = Tk()
                titre = Label(fen1, text="Vous venez de piger une nénette. Vous devez prendre automatiquement deux(2) jetons")
                titre.grid(padx=250, pady=250)
                bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
                bouton2.grid()
                bouton3 = Button(fen1, text="Quitter", command=exit)
                bouton3.grid()
                fen1.mainloop()
                #print("Vous venez de piger une nénette. Vous devez prendre automatiquement deux(2) jetons")
                v = min(2, self.nb_jetons_du_pot)
                self.joueurs[pos].ajouter_jetons(v)
                self.nb_jetons_du_pot -= v

            # routine pour déterminer le gagnant et le perdant après que ce joueur ait joué
            if i == 0:
                gagnant = pos
                perdant = pos
            else:
                if self.joueurs[pos].combinaison_actuelle < self.joueurs[perdant].combinaison_actuelle:
                    perdant = pos
                if ((self.joueurs[pos].combinaison_actuelle > self.joueurs[gagnant].combinaison_actuelle) or
                    (self.joueurs[pos].combinaison_actuelle == self.joueurs[gagnant].combinaison_actuelle)) :
                    gagnant = pos
            Partie.interface.afficher()

        # le perdant prends autant de jetons dans le pot que le gagnant a de point
        v = min(self.joueurs[gagnant].combinaison_actuelle.valeur, self.nb_jetons_du_pot)
        self.joueurs[perdant].ajouter_jetons(v)
        self.nb_jetons_du_pot -= v
        self.premier = perdant

        self.afficher_recapitulatif()
        return perdant, gagnant

    def jouer_tour_deuxieme_phase(self):
        """
        Cette méthode permet de faire le tour de tous les joueurs et leur permet de jouer pendant la décharge.
        Rappel: pendant la décharge chaque joueur peut lancer les  dés autant de fois que le premier joueur
        de la charge l'a fait. De plus, le gagnant du tour doit donner un nombre de jetons égale à son nombre de points au perdant du tour.
        Vous devez afficher à l'interface un récapitulatif des jetons des joueurs après le tour
        :return: un tuple d'entier qui correspond à l'index du perdant et celui du gagnant du tour
        """
        nb_maximum_lancer = 3
        for i in range(self.nb_total_joueurs):
            n = 3 if i == 0 else nb_maximum_lancer
            pos = (self.premier + i) % self.nb_total_joueurs
            fen1 = Tk()
            titre = Label(fen1, text="Tour de {}".format(self.joueurs[pos].nom))
            titre.grid(padx=250, pady=250)
            bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
            bouton2.grid()
            bouton3 = Button(fen1, text="Quitter", command=exit)
            bouton3.grid()
            fen1.mainloop()
            #Partie.interface.afficher("Tour de {}".format(self.joueurs[pos].nom))
            nb_lancer = self.joueurs[pos].jouer_tour(n)
            if i == 0:
                nb_maximum_lancer = nb_lancer
                gagnant, perdant = pos, pos
                fen1 = Tk()
                titre = Label(fen1, text="Le premier premier lanceur ayant fait {}, le nombre de "
                      "lancées pour ce tour est {}".format(nb_lancer, nb_lancer))
                titre.grid(padx=250, pady=250)
                bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
                bouton2.grid()
                bouton3 = Button(fen1, text="Quitter", command=exit)
                bouton3.grid()
                fen1.mainloop()
                #Partie.interface.afficher("Le premier premier lanceur ayant fait {}, le nombre de "
                      #"lancées pour ce tour est {}".format(nb_lancer, nb_lancer))
            else:
                if self.joueurs[pos].combinaison_actuelle < self.joueurs[perdant].combinaison_actuelle:
                    perdant = pos

                if ((self.joueurs[pos].combinaison_actuelle > self.joueurs[gagnant].combinaison_actuelle) or
                    (self.joueurs[pos].combinaison_actuelle == self.joueurs[gagnant].combinaison_actuelle)):
                    gagnant = pos

            Partie.interface.afficher()
        assert self.nb_total_joueurs > 1 and gagnant != perdant
        v = min(self.joueurs[gagnant].combinaison_actuelle.valeur, self.joueurs[gagnant].nb_jetons)
        self.joueurs[perdant].ajouter_jetons(v)
        self.joueurs[gagnant].retirer_jetons(v)
        self.premier = perdant
        self.afficher_recapitulatif()
        self.verifie_invariants()
        return perdant, gagnant

    def jouer(self):
        """
        Cette méthode permet de jouer une partie complète de 421.
        La partie doit commencer avec la détermination du joueur qui commence la décharge, puis il s'en suit la charge.
        Une fois la charge terminé, la décharge débute par le dernier perdant de la charge.
        Le jeu se termine dès qu'un joueur a tous les jetons de la partie
        """
        Partie.création_ficher_données(self)
        self.determiner_premier_lanceur()
        terminer = False
        fen1 = Tk()
        titre = Label(fen1, text="---- Début de la décharge----")
        titre.grid(padx=250, pady=250)
        bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton2.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()
        fen1.mainloop()
        #Partie.interface.afficher("*{:^40s}*".format("Début de la charge"))
        while self.nb_jetons_du_pot > 0:
            self.jouer_tour_premiere_phase()

        i = 0
        while (i < self.nb_total_joueurs):
            if self.verifier_gagnant(self.joueurs[i]):
                fen1 = Tk()
                titre = Label(fen1, text="{} a terminé la partie.".format(self.joueurs[i].nom))
                titre.grid(padx=250, pady=250)
                bouton2 = Button(fen1, text="Continuer", command=fen1.destroy)
                bouton2.grid()
                bouton3 = Button(fen1, text="Quitter", command=exit)
                bouton3.grid()
                fen1.mainloop()
                #Partie.interface.afficher("{} a terminé la partie.".format(self.joueurs[i].nom))
                self.retirer_joueur(i)
                if self.premier > i:
                    self.premier -= 1
            else:
                i += 1

        for i in range(self.nb_total_joueurs):
            if self.verifier_perdant(self.joueurs[i]):
                fen1 = Tk()
                titre = Label(fen1, text="Fin de la partie. {} a perdu et a tous les jetons du pot.".format(self.joueurs[i].nom))
                titre.grid(padx=250, pady=250)
                bouton3 = Button(fen1, text="Quitter", command=exit)
                bouton3.grid()
                fen1.mainloop()
                #Partie.interface.afficher("Fin de la partie. {} a perdu et a tous les jetons du pot.".format(self.joueurs[i].nom))
                return

        #Partie.interface.afficher("*{:^40s}*".format("Début de la décharge"))
        fen1 = Tk()
        titre = Label(fen1, text="---- Début de la décharge----")
        titre.grid(padx=250, pady=250)
        bouton1 = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton1.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()
        fen1.mainloop()
        while not terminer:
            perdant, gagnant = self.jouer_tour_deuxieme_phase()
            sortir_gagnant = self.verifier_gagnant(self.joueurs[gagnant])
            perdant_trouver = self.verifier_perdant(self.joueurs[perdant])
            if sortir_gagnant:
                fen1 = Tk()
                titre = Label(fen1, text="---- Un joueur est gagnant et a été retiré de la partie----")
                titre.grid(padx=250, pady=250)
                bouton2=Button(fen1,text="Continuer", command=fen1.destroy)
                bouton2.grid()
                bouton1 = Button(fen1, text="Quitter", command=exit)
                bouton1.grid()
                titre2 = Label(fen1, text="{} a terminé la partie.".format(self.joueurs[gagnant].nom))
                titre2.grid()
                fen1.mainloop()
                #Partie.interface.afficher("{} a terminé la partie.".format(self.joueurs[gagnant].nom))
                self.retirer_joueur(gagnant)
                if self.premier > gagnant:
                    self.premier -= 1

            if perdant_trouver:
                fen1 = Tk()
                titre = Label(fen1, text="---- Fin de la partie----")
                titre.grid(padx=250, pady=250)
                bouton1 = Button(fen1, text="Quitter", command=exit)
                bouton1.grid()
                fen1.mainloop()
                titre2 = Label(fen1, text="Fin de la partie. {} a perdu et a tous les jetons du pot.".format(self.joueurs[self.premier].nom))
                titre2.grid()
                fen1.mainloop()
                #Partie.interface.afficher("Fin de la partie. {} a perdu et a tous les jetons du pot.".format(self.joueurs[self.premier].nom))
                terminer = True

    def verifier_gagnant(self, joueur):
        """
        Cette méthode permet de déterminer si un joueur a gagné la partie, i.e qu'il n'a plus de jetons
        :param joueur: le joueur en question
        :return: True si le joueur n'a plus de jetons, False sinon
        """
        return joueur.nb_jetons == 0

    def verifier_perdant(self, joueur):
        """
        Cette méthode permet de déterminer si un joueur a perdu la partie
        :param joueur: le joueur en question
        :return: True si le joueur a tous les jetons de la partie, False sinon
        """
        return joueur.nb_jetons == NOMBRE_DE_JETONS_DU_JEU

    def retirer_joueur(self, position):
        """
        Retirer un joueur du jeu
        :param position: la position du joueur dans la liste des joueurs à retirer
        :return:
        """
        self.joueurs.pop(position)
        self.nb_total_joueurs -= 1

    def afficher_recapitulatif(self):
        """
        Affiche un tableau récapitulatif de la partie
        """
        fen1 = Tk()
        titre = Label(fen1, text="---- Récapitulatif de la partie ----")
        titre.grid(padx=250, pady=250)
        bouton = Button(fen1, text="Continuer", command=fen1.destroy)
        bouton.grid()
        bouton3 = Button(fen1, text="Quitter", command=exit)
        bouton3.grid()

        #n = 40
        #Partie.interface.afficher()
        #Partie.interface.afficher("{}\n|{:^38}|\n{}".format("_"*n, "Récapitulatif de la partie", "-"*n))
        #s = "|{:^27s}|{:^10d}|"
        pot_de_jetons = Label(fen1, text="---- Pots de jetons ----")
        pot_de_jetons.grid()
        pot_de_jetons2 = Label(fen1, text=str(self.nb_jetons_du_pot) + ":" + " " + "jetons")
        pot_de_jetons2.grid()

        #Partie.interface.afficher(s.format("POT DE JETONS", self.nb_jetons_du_pot))
        for j in sorted(self.joueurs, key=lambda x: x.nb_jetons, reverse=True):
            joueur=Label(fen1,text=str(j.nom) + ":" + " " + str(j.nb_jetons))
            joueur.grid()
            #Partie.interface.afficher(s.format(j.nom, j.nb_jetons))
        #Partie.interface.afficher("{}\n".format("-" * n))
        fen1.mainloop()

    def verifie_invariants(self):
        assert (sum([j.nb_jetons for j in self.joueurs]) + self.nb_jetons_du_pot) == NOMBRE_DE_JETONS_DU_JEU, \
            "Le nombre de jetons dans le jeu est actuellement différent de {}".format(NOMBRE_DE_JETONS_DU_JEU)

        assert len(self.joueurs) == self.nb_total_joueurs, "Le nombre de joueurs dans la partie est inexacte"
        assert self.premier < self.nb_total_joueurs



    def création_ficher_données(self):
        """
        Permet d'enregistrer divers attributs d'objets de joueurs dans un ficher text tout au long de l'exécution du programme

        """
        fichier_stats = open("421_statistiques.txt", "w")   #Créer et ouvre un .txt en écriture
        for j in (self.joueurs):                            #Inscrit les noms des joueurs dans le .txt
            infos_joueur = "Nom: " + str(j.nom) + "Premier lancer :" + "Nombre de jetons" + "\n"
            fichier_stats.write(infos_joueur)
           # for i in (self.joueurs):
        fichier_stats.close()

    #def obtenir_stats(self):


