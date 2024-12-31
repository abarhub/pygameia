# This is a sample Python script.
import random
import time
from copy import deepcopy

from tictactoe_game import TicTacToeGame, Games, Game, Coup, Partie, JoueurAleatoire, JoueurSimple, JoueurMinMax, \
    SerialisationGame, JoueurMinMax2


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def jeux():
    jeux = TicTacToeGame()
    jeux.joue(1, 0, 0)
    jeux.afficher()


def jeux2():
    jeux = TicTacToeGame()
    joueur = 1

    while (True):
        liste_coups = jeux.cases_possibles()
        n = random.randint(0, len(liste_coups) - 1)
        pos = liste_coups[n]
        jeux.joue(joueur, pos[0], pos[1])
        jeux.afficher()

        if jeux.finJeux():
            print("fin du jeux")
            gagnant = jeux.gagnant()
            if gagnant == 1:
                print("gagnant: joueur 1")
            elif gagnant == 2:
                print("gagnant: joueur 2")
            else:
                print("aucun gagnant")
            break

        if joueur == 1:
            joueur = 2
        else:
            joueur = 1


def coup_suivant(joueur, jeux, listeCoups, games):
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
            coup_suivant(joueur_suivant, jeux2, listeCoups2, games)

    pass


def jeux3():
    jeux = TicTacToeGame()
    joueur = 1
    games = Games()

    start = time.time()
    coup_suivant(joueur, jeux, [], games)

    print("duree:", time.ctime(time.time() - start)[11:19], " sec")

    print("nb de jeux: ", len(games.games))


def jeux4():
    nb_test=1
    resultats={1:0, 2:0, 0:0}

    print("calcul des coups ...")
    serial=SerialisationGame()
    games0=serial.getGames()
    # games0 = Games()
    # jeux = TicTacToeGame()
    # joueur = 1
    # start = time.time()
    # coup_suivant(joueur, jeux, [], games0)
    # print("duree:", time.ctime(time.time() - start)[11:19], " sec")

    print("debut partie ...")
    for i in range(nb_test):
        games = Games()
        joueur1 = JoueurAleatoire(games, 1)
        #joueur2 = JoueurAleatoire(games, 2)
        # joueur2=JoueurSimple(games, 2)
        #joueur2 = JoueurMinMax(games0, 2)
        joueur2 = JoueurMinMax2(games0, 2)
        partie = Partie(joueur1, joueur2)
        res=partie.partie()
        if res == 1:
            resultats[1] += 1
        elif res == 2:
            resultats[2] += 1
        else:
            resultats[0] += 1

    print("resultat: ", resultats)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jeux()
    jeux2()
    # jeux3()
    jeux4()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
