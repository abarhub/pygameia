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

    def clone_plateau(self) -> list[list[int]]:
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
                    pos = 0
                    for coup in partie.listeCoups:
                        if coup.plateau == plateau:
                            case = (coup.x, coup.y)
                            if pos == len(partie.listeCoups) - 1:
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
        # resultats_gagnant = []
        # resultats_null = []
        resultats = self.trouve_coups2(plateau)

        premier_gagnant = None
        premier_null = None
        for coup in resultats:
            game = coup[0]
            pos = coup[1]
            if game.noJoueurGagnant == self.no_joueur:
                if pos == len(game.listeCoups) - 1:
                    tmp = game.listeCoups[pos]
                    return tmp.x, tmp.y
                if premier_gagnant is None:
                    tmp = game.listeCoups[pos]
                    premier_gagnant = (tmp.x, tmp.y)
            elif game.noJoueurGagnant == 0:
                if premier_null is None:
                    tmp = game.listeCoups[pos]
                    premier_null = (tmp.x, tmp.y)
            else:
                if pos == len(game.listeCoups) - 1:
                    tmp = game.listeCoups[pos]
                    return tmp.x, tmp.y

        if premier_gagnant is not None:
            return premier_gagnant
        elif premier_null is not None:
            return premier_null

        # for coup in resultats:
        #     if coup[0].noJoueurGagnant == 0:
        #         tmp = coup[0].listeCoups[coup[1]]
        #         return tmp.x, tmp.y

        res = resultats[0]
        tmp = res[0].listeCoups[res[1]]
        return tmp.x, tmp.y

    def trouve_coups2(self, plateau: list[list[int]]) -> list[tuple[Game, int]]:
        liste2: list[tuple[Game, int]] = []
        for partie in self.games.games:
            pos = 0
            for coup in partie.listeCoups:
                if coup.plateau == plateau:
                    liste2.append((partie, pos))
                pos += 1

        return liste2


class JoueurMinMax3(JoueurAbstract):
    def __init__(self, games: Games, no_joueur: int, profondeur: int = 2):
        super().__init__(games, no_joueur)
        self.games: Games = games
        self.profondeur = profondeur

    def coup_suivant(self, jeux) -> tuple[int, int]:
        tmp = self.trouve_coups(jeux)
        return tmp

    def trouve_coups(self, jeux) -> tuple[int, int]:
        # plateau = jeux.clone_plateau()
        score = self.parcourt(jeux, self.no_joueur, self.profondeur, True)
        if score is None:
            raise Exception("Erreur de score")
        else:
            return score[1], score[2]
        # no_joueur = self.no_joueur
        # liste_cases = jeux.cases_possibles()
        # liste_coups = []
        # for coup in liste_cases:
        #     jeux2 = TicTacToeGame(jeux.clone_plateau())
        #     jeux2.joue(no_joueur, coup[0], coup[1])
        #     score = self.parcourt(jeux2, self.no_joueur, self.profondeur, True)
        #     liste_coups.append((coup[0], coup[1], score))
        #
        # score_max = None
        # resultat = None
        # for coup in liste_coups:
        #     if score_max is None or coup[2] > score_max:
        #         score_max = coup[2]
        #         resultat = (coup[0], coup[1])
        #
        # return resultat

    def parcourt(self, jeux: TicTacToeGame, no_joueur: int, niveaux: int, maxScore: bool) -> tuple[
                                                                                                 int, int, int] | None:
        #jeux2 = TicTacToeGame(jeux.clone_plateau())
        # no_joueur = no_joueur

        if jeux.finJeux():
            if jeux.gagnant() == self.no_joueur:
                return (100, 0, 0)
            elif jeux.gagnant() == 0:
                return (1, 0, 0)
            else:
                return (-100, 0, 0)

        liste_cases = jeux.cases_possibles()

        liste_score: list[tuple[int, int, int]] = []
        for coup in liste_cases:
            jeux3 = TicTacToeGame(jeux.clone_plateau())
            jeux3.joue(no_joueur, coup[0], coup[1])
            if niveaux <= 1:
                score = self.calcul_score(jeux3, no_joueur)
                liste_score.append((score, coup[0], coup[1]))
            else:
                no_joueur_suivant: int = self.autre_joueur(no_joueur)
                score_enfants = self.parcourt(jeux3, no_joueur_suivant, niveaux - 1, not maxScore)
                if score_enfants is not None:
                    score = score_enfants[0]
                    if not maxScore:
                        score = -score
                    liste_score.append((score, coup[0], coup[1]))

        if len(liste_score) == 0:
            return None
        elif maxScore:
            res: tuple[int, int, int] | None = None
            for score in liste_score:
                if res is None or res[0] > score[0]:
                    res = score
            return res
        else:
            res: tuple[int, int, int] | None = None
            for score in liste_score:
                if res is None or res[0] < score[0]:
                    res = score
            return res

    def calcul_score(self, game: TicTacToeGame, no_joueur: int) -> int:
        game_score = 0
        ajout_double = 1
        ajout_triple = 5
        for ligne in range(len(game.plateau)):

            if no_joueur == 1:
                nb_joueur1 = len([x for x in game.plateau[ligne] if x == JOUEUR1])
                if nb_joueur1 == 2:
                    game_score += ajout_double
                elif nb_joueur1 == 3:
                    game_score += ajout_triple
            elif no_joueur == 2:
                nb_joueur2 = len([x for x in game.plateau[ligne] if x == JOUEUR2])
                if nb_joueur2 == 2:
                    game_score += ajout_double
                elif nb_joueur2 == 3:
                    game_score += ajout_triple

        for colonne in range(len(game.plateau)):
            nb_joueur1 = 0
            nb_joueur2 = 0
            for n in range(len(game.plateau)):
                if game.plateau[n][colonne] == JOUEUR1:
                    nb_joueur1 += 1
                elif game.plateau[n][colonne] == JOUEUR2:
                    nb_joueur2 += 1
            if no_joueur == 1:
                if nb_joueur1 == 2:
                    game_score += ajout_double
                elif nb_joueur1 == 3:
                    game_score += ajout_triple
            elif no_joueur == 2:
                if nb_joueur2 == 2:
                    game_score += ajout_double
                elif nb_joueur2 == 3:
                    game_score += ajout_triple

        nb_joueur1 = 0
        nb_joueur2 = 0
        for n in range(len(game.plateau)):
            if game.plateau[n][n] == JOUEUR1:
                nb_joueur1 += 1
            elif game.plateau[n][n] == JOUEUR2:
                nb_joueur2 += 1
        if no_joueur == 1:
            if nb_joueur1 == 2:
                game_score += ajout_double
            elif nb_joueur1 == 3:
                game_score += ajout_triple
        elif no_joueur == 2:
            if nb_joueur2 == 2:
                game_score += ajout_double
            elif nb_joueur2 == 3:
                game_score += ajout_triple

        nb_joueur1 = 0
        nb_joueur2 = 0
        for n in range(len(game.plateau)):
            if game.plateau[2 - n][n] == JOUEUR1:
                nb_joueur1 += 1
            elif game.plateau[2 - n][n] == JOUEUR2:
                nb_joueur2 += 1
        if no_joueur == 1:
            if nb_joueur1 == 2:
                game_score += ajout_double
            elif nb_joueur1 == 3:
                game_score += ajout_triple
        elif no_joueur == 2:
            if nb_joueur2 == 2:
                game_score += ajout_double
            elif nb_joueur2 == 3:
                game_score += ajout_triple

        return game_score

    def autre_joueur(self, no_joueur: int) -> int:
        if no_joueur == 1:
            return 2
        elif no_joueur == 2:
            return 1
        else:
            raise Exception(f"joueur invalide{str(no_joueur)}")


class Partie:

    def __init__(self, joueur1: JoueurAbstract, joueur2: JoueurAbstract):
        self.joueur1: JoueurAbstract = joueur1
        self.joueur2: JoueurAbstract = joueur2

    def partie(self):
        jeux = TicTacToeGame()
        joueur: int = 1
        # games = Games()
        gagnant: int = -1
        liste_coups = []

        while True:
            pos = self.coup_suivant(jeux, joueur)
            jeux.joue(joueur, pos[0], pos[1])
            liste_coups.append((joueur, pos[0], pos[1]))
            # jeux.afficher()

            if jeux.finJeux():
                gagnant = jeux.gagnant()
                break

            if joueur == 1:
                joueur = 2
            else:
                joueur = 1

        jeux.afficher()
        print(f"liste des coups: {liste_coups}")
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

    def coup_suivant(self, joueur, jeux, listeCoups, games):
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
