from JeuCartesClassique import JeuCartesClassique


class Paquet(JeuCartesClassique):

    def __init__(self):
        super().__init__(True)  # ou JeuCartes.__init__(True)

    def ajouter(self, carte):
        self.cartes.append(carte)
