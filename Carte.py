class Carte:
    couleurs = ("Cœur", "Carreau", "Trèfle", "Pique")
    valeurs = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")

    def __init__(self, val, coul):
        try:
            Carte.validation(val, coul)
        except Exception as err:
            print(err)
            exit(1)

        self.__valeur = val
        self.__couleur = coul

    @staticmethod
    def validation(val, coul):
        if val < 2 or val > 14:
            raise Exception("Valeur de carte non reconnue")
        if coul < 0 or coul > 3:
            raise Exception("Couleur de carte non reconnue")

    def affiche(self):
        print(Carte.valeurs[self.__valeur], "de", Carte.couleurs[self.__couleur])

    def affiche_ascii(self):
        nom = str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]
        taille = len(nom) + 2
        print("\n")
        print("/", "-" * taille, "\\", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", nom, "|")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("\\", "-" * taille, "/", sep="")

    def __str__(self):
        #  return str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]
        return str(self.affiche_ascii())

    # Getter et Setter de Valeur

    def __getValeur(self):
        #  print("Passage dans getValeur !")
        return self.__valeur

    def __setValeur(self, val):
        #  print("Passage dans setValeur !")
        self.__valeur = val

    valeur = property(__getValeur, __setValeur)

    # Getter et Setter de Couleur

    def __getCouleur(self):
        #  print("Passage dans getCouleur !")
        return self.__couleur

    def __setCouleur(self, coul):
        #  print("Passage dans setCouleur !")
        self.__couleur = coul

    couleur = property(__getCouleur, __setCouleur)
