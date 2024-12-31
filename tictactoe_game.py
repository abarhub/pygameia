import pickle
import random
import time
from abc import ABC, abstractmethod
from copy import deepcopy
from pathlib import Path

JOUEUR1 = -1
JOUEUR2 = 1


class TicTacToeGame:

    def __init__(self, plateau=None):
        if plateau is None:
            self.plateau: list[list[int]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        else:
            self.plateau: list[list[int]] = deepcopy(plateau)

    def afficher(self):
        s = ""
        for row in self.plateau:
            s += "|"
            for col in row:
                if col == JOUEUR1:
                    s += "X"
                elif col == JOUEUR2:
                    s += "O"
                else:
                    s += " "
                s += "|"
            s += "\n"
        print("jeux:")
        print(s)

    def valeurCase(self, x, y) -> str:
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise Exception(f"la position n'est pas valide: x={x}, y={y}")
        n = self.plateau[x][y]
        return self.valeurCase2(n)

    def valeurCase2(self, n) -> str:
        if n == 0:
            return " "
        elif n == JOUEUR1:
            return "X"
        elif n == JOUEUR2:
            return "O"
        else:
            raise Exception(f"la valeur à la position n'est pas valide: {n}")

    def joue(self, noJoueur, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise Exception(f"la position n'est pas valide: x={x}, y={y}")
        if noJoueur < 1 or noJoueur > 2:
            raise Exception(f"le joueur doit avoir la valeur entre 1 et 2 (joueur={noJoueur})")
        if self.plateau[x][y] != 0:
            n = self.valeurCase(x, y)
            raise Exception(f"la position ({x},{y}) a deja une valeur: {n}")
        if noJoueur == 1:
            self.plateau[x][y] = -1
        elif noJoueur == 2:
            self.plateau[x][y] = 1

    def finJeux(self) -> bool:

        # for row in self.plateau:
        #     valeur = set()
        #     for col in row:
        #         valeur.add(col)
        #     if 0 not in valeur:
        #         if len(valeur) == 1:
        #             return True

        valeurLignes = dict()
        valeurColonnes = dict()
        diag1 = set()
        diag2 = set()
        caseIncomplete = False
        for i in range(3):
            for j in range(3):
                val = self.plateau[i][j]
                if i not in valeurLignes:
                    valeurLignes[i] = set()
                valeurLignes[i].add(val)
                if j not in valeurColonnes:
                    valeurColonnes[j] = set()
                valeurColonnes[j].add(val)
                if i == j:
                    diag1.add(val)
                if i + j == 2:
                    diag2.add(val)
                if val == 0:
                    caseIncomplete = True

        for valeur in valeurLignes:
            if len(valeurLignes[valeur]) == 1 and 0 not in valeurLignes[valeur]:
                return True

        for valeur in valeurColonnes:
            if len(valeurColonnes[valeur]) == 1 and 0 not in valeurColonnes[valeur]:
                return True

        if len(diag1) == 1 and 0 not in diag1:
            return True
        if len(diag2) == 1 and 0 not in diag2:
            return True

        if caseIncomplete:
            return False

        return True

    def cases_possibles(self) -> list[tuple[int, int]]:

        liste = []

        for i in range(3):
            for j in range(3):
                val = self.plateau[i][j]
                if val == 0:
                    liste.append((i, j))

        return liste

    def gagnant(self):

        # for row in self.plateau:
        #     valeur = set()
        #     for col in row:
        #         valeur.add(col)
        #     if 0 not in valeur:
        #         if len(valeur) == 1:
        #             return True

        valeurLignes = dict()
        valeurColonnes = dict()
        diag1 = set()
        diag2 = set()
        caseIncomplete = False
        for i in range(3):
            for j in range(3):
                val = self.plateau[i][j]
                if i not in valeurLignes:
                    valeurLignes[i] = set()
                valeurLignes[i].add(val)
                if j not in valeurColonnes:
                    valeurColonnes[j] = set()
                valeurColonnes[j].add(val)
                if i == j:
                    diag1.add(val)
                if i + j == 2:
                    diag2.add(val)
                if val == 0:
                    caseIncomplete = True

        for valeur in valeurLignes:
            if len(valeurLignes[valeur]) == 1 and 0 not in valeurLignes[valeur]:
                if JOUEUR1 in valeurLignes[valeur]:
                    return 1
                elif JOUEUR2 in valeurLignes[valeur]:
                    return 2
                else:
                    return 0

        for valeur in valeurColonnes:
            if len(valeurColonnes[valeur]) == 1 and 0 not in valeurColonnes[valeur]:
                if JOUEUR1 in valeurColonnes[valeur]:
                    return 1
                elif JOUEUR2 in valeurColonnes[valeur]:
                    return 2
                else:
                    return 0

        if len(diag1) == 1 and 0 not in diag1:
            if JOUEUR1 in diag1:
                return 1
            elif JOUEUR2 in diag1:
                return 2
            else:
                return 0
        if len(diag2) == 1 and 0 not in diag2:
            if JOUEUR1 in diag2:
                return 1
            elif JOUEUR2 in diag2:
                return 2
            else:
                return 0

        return 0

    def clone_plateau(self)->list[list[int]]:
        return deepcopy(self.plateau)


class Coup:
    def __init__(self, x: int, y: int, plateau: list[list[int]]) -> None:
        self.x: int = x
        self.y: int = y
        self.plateau: list[list[int]] = plateau

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __repr__(self):
        return self.__str__()


class Game:
    def __init__(self, noJoueurGagnant: int, listeCoups: list[Coup], plateau: list[list[int]]):
        self.noJoueurGagnant: int = noJoueurGagnant
        self.listeCoups: list[Coup] = listeCoups
        self.plateau: list[list[int]] = plateau


class Games:

    def __init__(self):
        self.games: list[Game] = []


class JoueurAbstract(ABC):

    def __init__(self, game: Games, no_joueur: int):
        self.game: Games = game
        self.no_joueur: int = no_joueur

    @abstractmethod
    def coup_suivant(self, jeux) -> tuple[int, int]:
        pass


class JoueurAleatoire(JoueurAbstract):

    def coup_suivant(self, jeux) -> tuple[int, int]:
        liste_coups = jeux.cases_possibles()
        n = random.randint(0, len(liste_coups) - 1)
        pos = liste_coups[n]
        return pos


class JoueurSimple(JoueurAbstract):

    def coup_suivant(self, jeux) -> tuple[int, int]:
        liste_coups = jeux.cases_possibles()
        pos = liste_coups[0]
        return pos


class JoueurMinMax(JoueurAbstract):
    def __init__(self, games: Games, no_joueur: int):
        super().__init__(games, no_joueur)
        self.games: Games = games

    def coup_suivant(self, jeux) -> tuple[int, int]:
        tmp = self.trouve_coups(jeux)
        return tmp

    def trouve_coups(self, jeux) -> tuple[int, int]:
        plateau = jeux.clone_plateau()
        resultats_gagnant = []
        resultats_null = []
        for partie in self.games.games:
            if True:
                if partie.noJoueurGagnant == self.no_joueur:
                    pos=0
                    for coup in partie.listeCoups:
                        if coup.plateau == plateau:
                            case = (coup.x, coup.y)
                            if pos==len(partie.listeCoups)-1:
                                return case
                            resultats_gagnant.append(case)
                        pos += 1
                elif partie.noJoueurGagnant == 0:
                    for coup in partie.listeCoups:
                        if coup.plateau == plateau:
                            case = (coup.x, coup.y)
                            resultats_null.append(case)

        if len(resultats_gagnant) > 0:
            return resultats_gagnant[0]
        elif len(resultats_null) > 0:
            return resultats_null[0]
        else:
            liste_coups = jeux.cases_possibles()
            return liste_coups[0]


class JoueurMinMax2(JoueurAbstract):
    def __init__(self, games: Games, no_joueur: int):
        super().__init__(games, no_joueur)
        self.games: Games = games

    def coup_suivant(self, jeux) -> tuple[int, int]:
        tmp = self.trouve_coups(jeux)
        return tmp

    def trouve_coups(self, jeux) -> tuple[int, int]:
        plateau = jeux.clone_plateau()
        resultats_gagnant = []
        resultats_null = []
        resultats=self.trouve_coups2(plateau)

        premier_gagnant=None
        for coup in resultats:
            game=coup[0]
            pos=coup[1]
            if game.noJoueurGagnant == self.no_joueur and pos==len(game.listeCoups)-1:
                tmp= game.listeCoups[pos]
                return tmp.x, tmp.y
            if premier_gagnant==None:
                tmp = game.listeCoups[pos]
                premier_gagnant=(tmp.x, tmp.y)

        if premier_gagnant!=None:
            return premier_gagnant

        for coup in resultats:
            if coup[0].noJoueurGagnant == 0:
                tmp= coup[0].listeCoups[coup[1]]
                return tmp.x, tmp.y

        res=resultats[0]
        tmp = res[0].listeCoups[res[1]]
        return tmp.x, tmp.y

    def trouve_coups2(self,plateau:list[list[int]])->list[tuple[Game, int]]:
        liste2:list[tuple[Game, int]]=[]
        for partie in self.games.games:
            pos = 0
            for coup in partie.listeCoups:
                if coup.plateau == plateau:
                    liste2.append((partie,pos))
                pos += 1

        return liste2


class Partie:

    def __init__(self, joueur1: JoueurAbstract, joueur2: JoueurAbstract):
        self.joueur1: JoueurAbstract = joueur1
        self.joueur2: JoueurAbstract = joueur2

    def partie(self):
        jeux = TicTacToeGame()
        joueur: int = 1
        # games = Games()
        gagnant: int = -1

        while True:
            pos = self.coup_suivant(jeux, joueur)
            jeux.joue(joueur, pos[0], pos[1])
            # jeux.afficher()

            if jeux.finJeux():
                gagnant = jeux.gagnant()
                break

            if joueur == 1:
                joueur = 2
            else:
                joueur = 1

        jeux.afficher()
        # print("fin du jeux")
        if gagnant == 1:
            print("gagnant: joueur 1")
        elif gagnant == 2:
            print("gagnant: joueur 2")
        else:
            print("aucun gagnant")
        return gagnant

    def coup_suivant(self, jeux, joueur):
        if joueur == 1:
            return self.joueur1.coup_suivant(jeux)
        elif joueur == 2:
            return self.joueur2.coup_suivant(jeux)
        else:
            raise Exception(f"joueur invalide: {joueur}")


class SerialisationGame:
    filename: str = "data/games.pickle"

    def serialise(self, games: Games):
        with open(self.filename, "wb") as outfile:
            # "wb" argument opens the file in binary mode
            pickle.dump(games, outfile)

    def deserialise(self) -> Games:
        with open(self.filename, "rb") as infile:
            games = pickle.load(infile)
            return games

    def getGames(self) -> Games:
        my_file = Path(self.filename)
        if my_file.is_file():
            print("recuperation des coups sur le fs ...")
            games = self.deserialise()
            return games
        else:
            print("calcul des coups ...")
            games0 = Games()
            jeux = TicTacToeGame()
            joueur = 1
            start = time.time()
            self.coup_suivant(joueur, jeux, [], games0)
            print("duree:", time.ctime(time.time() - start)[11:19], " sec")
            self.serialise(games0)
            return games0

    def coup_suivant(self,joueur, jeux, listeCoups, games):
        liste_coups = jeux.cases_possibles()

        for coup in liste_coups:
            jeux2 = TicTacToeGame(jeux.clone_plateau())
            listeCoups2 = deepcopy(listeCoups)
            listeCoups2.append(Coup(coup[0], coup[1], jeux2.clone_plateau()))
            jeux2.joue(joueur, coup[0], coup[1])
            fin = False
            if jeux2.finJeux():
                # print("fin du jeux")
                gagnant = jeux2.gagnant()
                # if gagnant == 1:
                #     print(f"gagnant: joueur 1 : {listeCoups2}")
                # elif gagnant == 2:
                #     print(f"gagnant: joueur 2 : {listeCoups2}")
                # else:
                #     print(f"aucun gagnant : {listeCoups2}")
                fin = True
                game = Game(gagnant, listeCoups2, jeux2.clone_plateau())
                games.games.append(game)
            else:
                if joueur == 1:
                    joueur_suivant = 2
                else:
                    joueur_suivant = 1
                self.coup_suivant(joueur_suivant, jeux2, listeCoups2, games)
