from JeuCartes import JeuCartes
from Carte import Carte


class JeuCartesClassique(JeuCartes):

    def initialiser(self):
        for val in range(2, 15):
            for coul in range(4):
                self.cartes.append(Carte(val, coul))
