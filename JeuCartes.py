from Carte import Carte
from random import shuffle


class JeuCartes:

    def __init__(self, vide=False):
        if self.__class__ is JeuCartes:
            raise Exception("Construction directe interdite")
        else:
            self.__cartes = []
            if not vide:
                self.initialiser()

    def initialiser(self):
        pass

    def __str__(self):
        carte = ""
        for i in range(len(self.__cartes)):
            if carte == "":
                carte = str(self.__cartes[i])
            else:
                carte += ", " + str(self.__cartes[i])
        return carte

    def melanger(self):
        shuffle(self.__cartes)

    def tirer(self):
        try:
            return self.__cartes.pop(0)
        except IndexError:
            print("Il n'y a plus de carte dans le jeu !")
            raise IndexError
            return None

    def __getCartes(self):
        return self.__cartes

    def __setCartes(self, cartes):
        if len(self.__cartes) > 52:
            raise Exception("Jeu Complet")
        self.__cartes.append(cartes)

    cartes = property(__getCartes, __setCartes)

    def __add__(self, cartes):
        print("__ADD__ surcharge d'operateur")
        self.ajouter(cartes)

    def __len__(self):
        return len(self.__cartes)
