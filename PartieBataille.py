from Joueur import Joueur
from JeuCartesClassique import JeuCartesClassique


class PartieBataille:
    cJ1 = []
    cJ2 = []

    def __init__(self, nom1, prenom1, nom2, prenom2):
        self.__nom1 = nom1
        self.__prenom1 = prenom1
        self.__nom2 = nom2
        self.__prenom2 = prenom2
        self.__jeuDeCartes = JeuCartesClassique()

        self.__J1 = Joueur(nom1, prenom1)
        self.__J2 = Joueur(nom2, prenom2)

    def distribuer(self):
        while True:
            self.__J1.ajouter(self.__jeuDeCartes.tirer())
            self.__J2.ajouter(self.__jeuDeCartes.tirer())

    def melanger(self):
        self.__jeuDeCartes.melanger()

    def demarrerPartie(self):
        try:
            self.melanger()
            self.distribuer()
        except IndexError as err:
            print(err)
            while True:
                self.main()

    def bataille(self):
        c2J1 = self.__J1.tirer()
        c2J2 = self.__J2.tirer()
        c3J1 = self.__J1.tirer()
        c3J2 = self.__J2.tirer()
        print(c3J1, "\r vs ", c3J2, "\r")
        if c3J1.valeur < c3J2.valeur:
            self.__J2.ajouter(c3J1)
            self.__J2.ajouter(c3J2)
            self.__J2.ajouter(c2J1)
            self.__J2.ajouter(c2J2)
            print(self.__J2.nom, self.__J2.prenom, " gagne la bataille et récupère les cartes\n")
            self.__J2.victoire += 1
            self.__J1.defaite += 1
            for i in range(len(self.cJ2)):
                self.__J2.ajouter(self.cJ2.pop(0))
                self.__J2.ajouter(self.cJ1.pop(0))
            print("Nombres cartes Joueur 1 : ", len(self.__J1.paquet.cartes))
            print("Nombres cartes Joueur 2 : ", len(self.__J2.paquet.cartes))
            input("next\n")
            self.main()
        elif c3J1.valeur > c3J2.valeur:
            self.__J1.ajouter(c3J1)
            self.__J1.ajouter(c3J2)
            self.__J1.ajouter(c2J1)
            self.__J1.ajouter(c2J2)
            print(self.__J1.nom, self.__J1.prenom, " gagne la bataille et récupère les cartes\n")
            self.__J1.victoire += 1
            self.__J2.defaite += 1
            for i in range(len(self.cJ2)):
                self.__J1.ajouter(self.cJ2.pop(0))
                self.__J1.ajouter(self.cJ1.pop(0))
            print("Nombres cartes Joueur 1 : ", len(self.__J1.paquet.cartes))
            print("Nombres cartes Joueur 2 : ", len(self.__J2.paquet.cartes))
            input("next\n")
            self.main()
        else:
            print("Bataille\n")
            self.cJ1.append(c2J1)
            self.cJ1.append(c3J1)
            self.cJ2.append(c2J2)
            self.cJ1.append(c3J2)
            self.bataille()

    def finPartie(self):
        ScoreVJ1 = self.__J1.victoire
        ScoreVJ2 = self.__J2.victoire
        ScoreDJ1 = self.__J1.defaite
        ScoreDJ2 = self.__J2.defaite
        print("Le score de la partie est : ", ScoreVJ1, ScoreDJ1, " pour le joueur 1\n", ScoreVJ2, ScoreDJ2, " pour le joueur 2\n")
        exit(1)

    def main(self):
        while len(self.__J1.paquet.cartes) != 0 or len(self.__J2.paquet.cartes) != 0:
            if len(self.__J1.paquet.cartes) != 0:
                cJ1 = self.__J1.tirer()
            else:
                print(self.__J1.nom, "a perdu")
                self.finPartie()
            if len(self.__J2.paquet.cartes) != 0:
                cJ2 = self.__J2.tirer()
            else:
                print(self.__J2.nom, "a perdu")
                self.finPartie()
            print(cJ1, "\r vs ", cJ2, "\r ")
            if cJ1.valeur < cJ2.valeur:
                self.__J2.ajouter(cJ1)
                self.__J2.ajouter(cJ2)
                print(self.__J2.nom, self.__J2.prenom, " gagne et récupère les cartes\n")
                self.__J2.victoire += 1
                self.__J1.defaite += 1
                print("Nombres cartes Joueur 1 : ", len(self.__J1.paquet.cartes))
                print("Nombres cartes Joueur 2 : ", len(self.__J2.paquet.cartes))
            elif cJ1.valeur > cJ2.valeur:
                self.__J1.ajouter(cJ1)
                self.__J1.ajouter(cJ2)
                print(self.__J1.nom, self.__J1.prenom, " gagne et récupère les cartes\n")
                self.__J1.victoire += 1
                self.__J2.defaite += 1
                print("Nombres cartes Joueur 1 : ", len(self.__J1.paquet.cartes))
                print("Nombres cartes Joueur 2 : ", len(self.__J2.paquet.cartes))
            else:
                print("Bataille\n")
                self.bataille()
            input("next\n")
        self.finPartie()
