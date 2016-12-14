from jeu421.interface import Interface
from jeu421.combinaison import *
from random import randint


class Joueur:
    """
    Classe représentant un joueur de 421. Un joueur a les attributs
    - nom: son nom
    - nb_jetons: son nombre de jetons, entier entre 0 et 21
    - combinaison actuelle: un objet de la classe Combinaison
    La classe a un attribut static interface qui est l'interface de communication entre les joueurs et le programme

    """
    interface = Interface()

    def __init__(self, nom):
        """
        Constructeur de la classe, doit initialiser le nom du joueur à la valeur passée en paramètre.
        Le nombre de jetons à zéro, et la combinaison_actuelle à None
        :param nom: nom du joueur
        """
        self.nom = nom
        self.nb_jetons = 0
        self.combinaison_actuelle = None

    def lancer_des(self, nombre_des):
        """
        Méthode permettant à un joeur de lancer dés
        :param nombre_des: nombre de dés à lancer
        :return: une liste de longueur nombre_des contenant les valeurs de chaque dés selon le lancé
        """
        return [randint(1, 6) for _ in range(nombre_des)]

    def jouer_tour(self, nb_maximum_lancer=3):
        """
        Cette méthode permet à un joueur de jouer lorsque c'est son tour dans une partie, en lançant les dés.
        Vous devez demandez au joueur de lancer des dés, de choisir les dés à relancer et puis changer l'attribut combinaison actuelle du
        :param nb_maximum_lancer: le nombre maximum de lancés auquel le joueur a droit lors de ce tour.
        :return: retourne le nombre de lancés que le joueur a fait.
        """
        objectif_est_atteint = False
        i = 0
        nb_des_a_lancer = NOMBRE_DES_DU_JEU
        resultat_lancer = []
        while (not objectif_est_atteint) and (i < nb_maximum_lancer):
            Joueur.interface.demander_entree("Appuyer sur la touche Enter pour lancer!")
            temp = self.lancer_des(nb_des_a_lancer)
            Joueur.interface.afficher("Lancé {} = {}".format(i+1, temp))
            resultat_lancer += temp
            possibilte_de_relancer = (i < nb_maximum_lancer - 1)
            if possibilte_de_relancer:
                des_a_relancer = Joueur.interface.choisir_des_a_relancer(resultat_lancer)
                nb_des_a_lancer = len(des_a_relancer)
                if des_a_relancer == []:
                    objectif_est_atteint = True
                else:
                    for v in des_a_relancer:
                        resultat_lancer.remove(v)
            i += 1
        self.combinaison_actuelle = Combinaison(resultat_lancer)
        Joueur.interface.afficher("Combinaison finale = {}, soit {} points".format(self.combinaison_actuelle,
                                                               self.combinaison_actuelle.valeur))
        return i

    def ajouter_jetons(self, nb_jetons):
        """
        Cette méthode permet d'ajouter un nombre de jetons à ceux déjà détenus par le joueur
        :param nb_jetons: nombre de jetons à ajouter
        :return aucun
        """
        self.nb_jetons += nb_jetons

    def retirer_jetons(self, nb_jetons):
        """
        Cette méthode permet de retirer un nombre de jetons de ceux détenus par le joueur
        :param nb_jetons: nombre de jetons à retirer
        :return aucun
        """
        self.nb_jetons -= nb_jetons

    def __str__(self):
        """
        Cette méthode retourne une représentation d'un joueur. le format est "nom_du_joueur - nombre_de_jetons"
        Cette méthode est appelée lorsque vous faites print(A) où A est un joueur
        :return: retourne une chaine de caractère qui est une représentation.
            Exemple: "Joueur1 - 12"
        """
        return "{} - {}".format(self.nom, self.nb_jetons)

    def __le__(self, other):
        """
        Comparaison ( <= ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est inférieur ou égal à celui de other
        """
        return self.nb_jetons <= other.nb_jetons

    def __ge__(self, other):
        """
        Comparaison ( >= ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est supérieur ou égal à celui de other
        """
        return self.nb_jetons >= other.nb_jetons

    def __lt__(self, other):
        """
        Comparaison ( < ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est inférieur à celui de other
        """
        return self.nb_jetons < other.nb_jetons

    def __gt__(self, other):
        """
        Comparaison ( > ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est supérieur à celui de other
        """
        return self.nb_jetons > other.nb_jetons

    def __eq__(self, other):
        """
        Comparaison ( == ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est égal à celui de other
        """
        return self.nb_jetons == other.nb_jetons

    def verifier_invariants(self):
        assert 0 <= self.nb_jetons <= NOMBRE_DE_JETONS_DU_JEU, "Le nombre de jetons du joueur est incorrect"

class JoueurAlgo(Joueur):
    """
    Classe représentant un joueur fictif qui applique une stratégie de type 1. Il visera donc toujours à obtenir la
    combinaison du 421. Cette classe hérite de la classe Joueur.
    """
    def __init__(self):



        super().__init__(self)

    def choix_421(tri=False):
        """
        Fonction qui simule un lancer lorsque l'utilisateur a choisi la combinaison 421.
        :param tri: (bool) Si True, on trie les couples.
        :return: (list) Résultat des lancés de dés.
        """
        combinaison_gagnante = [4, 2, 1]
        combinaison_finale = []
        nombre_tirage = 0
        lancer_1 = ""
        lancer_2 = ""
        lancer_3 = ""
        while nombre_tirage != 3:
            # On ne veut pas faire plus que 3 lancers.
            tirage = Joueur.lancer_des(Joueur, 3-len(combinaison_finale))
            nombre_tirage += 1
            if nombre_tirage == 1:
                lancer_1 = tirage
                for i in range(len(tirage)):
                    if tirage[i] in combinaison_gagnante:
                        if tirage[i] not in combinaison_finale:
                            # On ne veut garder qu'un 4, un 2 et un 1.
                            combinaison_finale.append(tirage[i])
            elif nombre_tirage == 2:
                lancer_2 = tirage

                for i in range(len(tirage)):
                    if tirage[i] in combinaison_gagnante:
                        if tirage[i] not in combinaison_finale:
                            # On ne veut garder qu'un 4, un 2 et un 1.
                            combinaison_finale.append(tirage[i])
            elif nombre_tirage == 3:
                # Si c'est le dernier lancer, on est pris avec nos derniers résultats.
                lancer_3 = tirage
                for i in range(len(tirage)):
                    combinaison_finale.append(tirage[i])
        if tri:
            combinaison_finale.sort(reverse=True)
        return combinaison_finale

print(JoueurAlgo.choix_421(tri=True))

print("ok")
