import unittest

from tictactoe_game import TicTacToeGame, JoueurMinMax3, Games


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        jeux = TicTacToeGame()
        jeux.joue(1, 0, 0)

        self.assertEqual(-1, jeux.plateau[0][0])  # add assertion here
        for i in range(2):
            for j in range(2):
                if i != 0 and j != 0:
                    self.assertEqual(0, jeux.plateau[i][j])

    def test_case1_bis(self):
        jeux = TicTacToeGame()
        jeux.joue(2, 0, 0)

        self.assertEqual(1, jeux.plateau[0][0])  # add assertion here
        for i in range(2):
            for j in range(2):
                if i != 0 and j != 0:
                    self.assertEqual(0, jeux.plateau[i][j])


    def test2(self):
        jeux = TicTacToeGame()
        jeux.joue(1, 0, 0)
        jeux.joue(1, 1, 0)
        jeux.joue(1, 2, 0)

        self.assertEqual(-1, jeux.plateau[0][0])
        self.assertEqual(-1, jeux.plateau[1][0])
        self.assertEqual(-1, jeux.plateau[2][0])
        for i in range(2):
            for j in range(2):
                if j != 0:
                    self.assertEqual(0, jeux.plateau[i][j])


    def test3(self):
        jeux = TicTacToeGame()
        jeux.joue(2, 0, 0)
        jeux.joue(1, 0, 2)

        jeux.joue(2, 1, 0)
        jeux.joue(1, 1, 1)
        jeux.joue(1, 1, 2)

        jeux.joue(2, 2, 0)
        jeux.joue(1, 2, 1)
        jeux.joue(2, 2, 2)

        self.assertEqual(1, jeux.plateau[0][0])
        self.assertEqual(0, jeux.plateau[0][1])
        self.assertEqual(-1, jeux.plateau[0][2])

        self.assertEqual(1, jeux.plateau[1][0])
        self.assertEqual(-1, jeux.plateau[1][1])
        self.assertEqual(-1, jeux.plateau[1][2])

        self.assertEqual(1, jeux.plateau[2][0])
        self.assertEqual(-1, jeux.plateau[2][1])
        self.assertEqual(1, jeux.plateau[2][2])

        self.assertEqual(True, jeux.finJeux())
        self.assertEqual(2, jeux.gagnant())

    def test4(self):
        jeux = TicTacToeGame()
        jeux.joue(1, 0, 0)
        jeux.joue(2, 0, 1)
        jeux.joue(2, 0, 2)

        jeux.joue(2, 1, 0)
        jeux.joue(1, 1, 1)
        jeux.joue(1, 1, 2)

        jeux.joue(1, 2, 0)
        jeux.joue(1, 2, 1)
        jeux.joue(2, 2, 2)

        self.assertEqual(-1, jeux.plateau[0][0])
        self.assertEqual(1, jeux.plateau[0][1])
        self.assertEqual(1, jeux.plateau[0][2])

        self.assertEqual(1, jeux.plateau[1][0])
        self.assertEqual(-1, jeux.plateau[1][1])
        self.assertEqual(-1, jeux.plateau[1][2])

        self.assertEqual(-1, jeux.plateau[2][0])
        self.assertEqual(-1, jeux.plateau[2][1])
        self.assertEqual(1, jeux.plateau[2][2])

        self.assertEqual(True, jeux.finJeux())
        self.assertEqual(0, jeux.gagnant())

    def test5(self):
        jeux = TicTacToeGame()
        jeux.joue(1, 0, 0)
        jeux.joue(1, 0, 1)
        jeux.joue(1, 0, 2)

        jeux.joue(2, 1, 0)
        jeux.joue(2, 1, 1)
        #jeux.joue(1, 1, 2)

        jeux.joue(1, 2, 0)
        #jeux.joue(1, 2, 1)
        jeux.joue(2, 2, 2)

        self.assertEqual(-1, jeux.plateau[0][0])
        self.assertEqual(-1, jeux.plateau[0][1])
        self.assertEqual(-1, jeux.plateau[0][2])

        self.assertEqual(1, jeux.plateau[1][0])
        self.assertEqual(1, jeux.plateau[1][1])
        self.assertEqual(0, jeux.plateau[1][2])

        self.assertEqual(-1, jeux.plateau[2][0])
        self.assertEqual(0, jeux.plateau[2][1])
        self.assertEqual(1, jeux.plateau[2][2])

        self.assertEqual(True, jeux.finJeux())
        self.assertEqual(1, jeux.gagnant())

    def test6(self):
        jeux = TicTacToeGame()
        jeux.joue(2, 0, 0)
        jeux.joue(2, 0, 1)
        jeux.joue(2, 0, 2)

        jeux.joue(1, 1, 0)
        jeux.joue(1, 1, 1)
        #jeux.joue(1, 1, 2)

        jeux.joue(2, 2, 0)
        #jeux.joue(1, 2, 1)
        jeux.joue(1, 2, 2)

        self.assertEqual(1, jeux.plateau[0][0])
        self.assertEqual(1, jeux.plateau[0][1])
        self.assertEqual(1, jeux.plateau[0][2])

        self.assertEqual(-1, jeux.plateau[1][0])
        self.assertEqual(-1, jeux.plateau[1][1])
        self.assertEqual(0, jeux.plateau[1][2])

        self.assertEqual(1, jeux.plateau[2][0])
        self.assertEqual(0, jeux.plateau[2][1])
        self.assertEqual(-1, jeux.plateau[2][2])

        self.assertEqual(True, jeux.finJeux())
        self.assertEqual(2, jeux.gagnant())


    def test7(self):
        jeux=self.initialise_jeux(liste_coups=[(0,1),(0,0),(2,1)])
        jeux.afficher()
        games = Games()
        joueur2 = JoueurMinMax3(games, 2)
        #joueur2.parcourt(jeux,2,1,True)
        # corriger le calcul du score
        tmp=joueur2.trouve_coups(jeux)
        print(tmp)
        self.assertEqual((1,1), tmp)

    def test8(self):
        #jeux=TicTacToeGame()
        param_list=[
            ([(0,1),(0,0),(2,1)],2,(1,1),"test1"),
            #([(1, 2, 0), (2, 0, 0), (1, 1, 2), (2, 0, 1), (1, 0, 2), (2, 1, 0), (1, 2, 1)], 2, (1, 1), "test2"),
        ]
        for (liste_coups, no_joueur,pos, msg_test) in param_list:
            with self.subTest(msg=f"test {msg_test}",param=[liste_coups, no_joueur,pos]):
                jeux = self.initialise_jeux(liste_coups=liste_coups)
                jeux.afficher()
                games = Games()
                joueur = JoueurMinMax3(games, no_joueur)
                case_choisie=joueur.trouve_coups(jeux)
                self.assertEqual(pos, case_choisie, msg=f"jeux {msg_test}:\n{jeux.to_string()}\npos:{pos}\ncase_choisie:{case_choisie}")

    def initialise_jeux(self, liste_coups=None) -> TicTacToeGame:
        if liste_coups is None:
            liste_coups = []
        jeux = TicTacToeGame()
        no_joueur=1
        for coup in liste_coups:
            jeux.joue(no_joueur, coup[0], coup[1])
            if no_joueur==1:
                no_joueur=2
            else:
                no_joueur=1

        return jeux


if __name__ == '__main__':
    unittest.main()
