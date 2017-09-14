## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
#make 4 test classes
class TestCard(unittest.TestCase):
    def setUp(self):
        self.king_hearts = Card(2,13)

    def test_suit_type(self):
        self.assertEqual(self.king_hearts.suit, "Hearts", 'seeing if the suit is right')

    def test_suit_list(self):
        self.assertEqual(type(self.king_hearts.suit_names), type([]), "making sure suit type is right")

    def test_rank_num(self):
        self.assertEqual(type(self.king_hearts.rank_num), int, "checking if this returns an integer for rank number")

    def test_rank(self):
        self.assertEqual(self.king_hearts.rank, "King")

    def test_return_string(self):
        self.assertEqual(str(self.king_hearts), "King of Hearts")

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_self_cards_type(self):
        self.assertEqual(type(self.deck.cards), list)

class TestWar(unittest.TestCase):
    def test_war_type(self):
        war = play_war_game(testing=True)
        self.assertEqual(type(war), tuple)

    def test_war_first_position_of_tuple(self):
        war = play_war_game(testing=True)
        self.assertTrue(war[0] in ['Player1', 'Player2', 'Tie'])

    def test_war_two_integers(self):
        war = play_war_game(testing=True)
        self.assertEqual(type(war[1]), int)
        self.assertEqual(type(war[2]), int)

    def test_war_winners(self):
        war = play_war_game(testing=True)
        if war[0] == 'Player1':
            self.assertTrue(war[1]>war[2])
        elif war[0] == 'Player2':
            self.assertTrue(war[2]>war[1])
        else:
            self.assertTrue(war[1]==war[2])


#if player one won, player one score should be more than player two








unittest.main(verbosity=2)
