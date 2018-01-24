from Paquet import Paquet


class Joueur:

    def __init__(self, n, p):
        self.__nom = n
        self.__prenom = p
        self.__victoire = 0
        self.__defaite = 0
        self.__paquet = Paquet()

    def tirer(self):
        return self.__paquet.tirer()

    def ajouter(self, carte):
        self.__paquet.ajouter(carte)

    def __add__(self, carte):
        self.ajouter(carte)

    def __setNom(self, nom):
        self.__nom = nom

    def __getNom(self):
        return self.__nom

    nom = property(__getNom, __setNom)

    def __setPrenom(self, prenom):
        self.__prenom = prenom

    def __getPrenom(self):
        return self.__prenom

    prenom = property(__getPrenom, __setPrenom)

    def __setVictoire(self, victoire):
        self.__victoire = victoire

    def __getVictoire(self):
        return self.__victoire

    victoire = property(__getVictoire, __setVictoire)

    def __setDefaite(self, defaite):
        self.__defaite = defaite

    def __getDefaite(self):
        return self.__defaite

    defaite = property(__getDefaite, __setDefaite)

    def __getPaquet(self):
        return self.__paquet

    paquet = property(__getPaquet)
