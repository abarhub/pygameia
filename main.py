# This is a sample Python script.
import random

from tictactoe_game import TicTacToeGame


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def jeux():
    jeux = TicTacToeGame()
    jeux.joue(1,0,0)
    jeux.afficher()


def jeux2():
    jeux = TicTacToeGame()
    joueur=1

    while(True):
        liste_coups = jeux.cases_possibles()
        n=random.randint(0,len(liste_coups)-1)
        pos=liste_coups[n]
        jeux.joue(joueur,pos[0],pos[1])
        jeux.afficher()

        if jeux.finJeux():
            print("fin du jeux")
            gagnant=jeux.gagnant()
            if gagnant==1:
                print("gagnant: joueur 1")
            elif gagnant==2:
                print("gagnant: joueur 2")
            else:
                print("aucun gagnant")
            break

        if joueur==1:
            joueur = 2
        else:
            joueur = 1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    jeux()
    jeux2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
