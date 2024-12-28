# This is a sample Python script.
import random

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

JOUEUR1 = -1
JOUEUR2 = 1


class TicTacToeGame:

    def __init__(self):
        self.plateau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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

    def valeurCase(self,x,y):
        if x<0 or x>2 or y<0 or y>2:
            raise Exception(f"la position n'est pas valide: x={x}, y={y}")
        n=self.plateau[x][y]
        return self.valeurCase2(n)

    def valeurCase2(self,n):
        if n==0:
            return " "
        elif n==JOUEUR1:
            return "X"
        elif n==JOUEUR2:
            return "O"
        else:
            raise Exception(f"la valeur à la position n'est pas valide: {n}")

    def joue(self,noJoueur,x,y):
        if x<0 or x>2 or y<0 or y>2:
            raise Exception(f"la position n'est pas valide: x={x}, y={y}")
        if noJoueur<1 or noJoueur>2:
            raise Exception(f"le joueur doit avoir la valeur entre 1 et 2 (joueur={noJoueur})")
        if self.plateau[x][y] !=0:
            n=self.valeurCase(x,y)
            raise Exception(f"la position ({x},{y}) a deja une valeur: {n}")
        if noJoueur == 1:
            self.plateau[x][y]=-1
        elif noJoueur == 2:
            self.plateau[x][y]=1

    def finJeux(self):

        for row in self.plateau:
            valeur = set()
            for col in row:
                valeur.add(col)
            if 0 not in valeur:
                if len(valeur) == 1:
                    return True

        valeurLignes=dict()
        valeurColonnes = dict()
        diag1 = set()
        diag2 = set()
        caseIncomplete=False
        for i in range(3):
            for j in range(3):
                val=self.plateau[i][j]
                if i not in valeurLignes:
                    valeurLignes[i] = set()
                valeurLignes[i].add(val)
                if j not in valeurColonnes:
                    valeurColonnes[j] = set()
                valeurColonnes[j].add(val)
                if i==j:
                    diag1.add(val)
                if i+j==2:
                    diag2.add(val)
                if val==0:
                    caseIncomplete=True

        for valeur in valeurLignes:
            if len(valeurLignes[valeur]) == 1 and 0 not in valeurLignes[valeur]:
                return True

        for valeur in valeurColonnes:
            if len(valeurColonnes[valeur]) == 1 and 0 not in valeurColonnes[valeur]:
                return True

        if len(diag1)==1 and 0 not in diag1:
            return True
        if len(diag2)==1 and 0 not in diag2:
            return True

        if caseIncomplete:
            return False

        return True

    def cases_possibles(self):

        liste=[]

        for i in range(3):
            for j in range(3):
                val = self.plateau[i][j]
                if val==0:
                    liste.append((i, j))

        return liste

    def gagnant(self):

        for row in self.plateau:
            valeur = set()
            for col in row:
                valeur.add(col)
            if 0 not in valeur:
                if len(valeur) == 1:
                    return True

        valeurLignes=dict()
        valeurColonnes = dict()
        diag1 = set()
        diag2 = set()
        caseIncomplete=False
        for i in range(3):
            for j in range(3):
                val=self.plateau[i][j]
                if i not in valeurLignes:
                    valeurLignes[i] = set()
                valeurLignes[i].add(val)
                if j not in valeurColonnes:
                    valeurColonnes[j] = set()
                valeurColonnes[j].add(val)
                if i==j:
                    diag1.add(val)
                if i+j==2:
                    diag2.add(val)
                if val==0:
                    caseIncomplete=True

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

        if len(diag1)==1 and 0 not in diag1:
            if JOUEUR1 in diag1:
                return 1
            elif JOUEUR2 in diag1:
                return 2
            else:
                return 0
        if len(diag2)==1 and 0 not in diag2:
            if JOUEUR1 in diag2:
                return 1
            elif JOUEUR2 in diag2:
                return 2
            else:
                return 0

        return 0



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
