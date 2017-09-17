## Do not change import statements.
import unittest
from helper_functions import *

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

    def test_deck_self_cards_type(self):
        self.deck = Deck()
        self.assertEqual(type(self.deck.cards), list)

    def test_deck_self_cards_instance_of_Cards(self):
        self.deck = Deck()
        self.assertIsInstance(self.deck.cards[0], Card)

    def test_deck_self_cards_instance_of_Cards_part_2(self): #testing all elements
        self.deck = Deck()
        for card_object in self.deck.cards:
            self.assertIsInstance(card_object, Card)

    def test_deck_self_cards_length(self):
        self.deck = Deck()
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_return_52_line_string(self):
        self.deck = Deck()
        d_string = str(self.deck)
        d_list = d_string.split('\n')
        self.assertEqual(len(d_list),52)

    def test_pop_card(self):
        self.deck = Deck()
        for x in range(0,52):
            self.deck.pop_card()
        self.assertEqual(len(self.deck.cards),0)

    def test_shuffle(self):
        first_deck = Deck()
        second_deck = Deck()
        first_deck.shuffle()
        self.assertFalse(first_deck.cards == second_deck.cards)

    def test_sort_cards(self):
        orig_deck = Deck()
        another_deck = Deck()
        another_deck.shuffle()
        another_deck.sort_cards()
        self.assertTrue(str(orig_deck)==str(another_deck))

    def test_deal_hand(self):
        deck = Deck()
        try:
            the_deal = deck.deal_hand(52)
            alist = [str(card) for card in the_deal]

        except:
            self.assertRaises(IndexError, the_deal)

    def test_deal_hand2(self):
        deck = Deck()
        my_hand = deck.deal_hand(5)
        self.assertTrue(len(my_hand), 5)
        print([str(c) for c in my_hand])

    def test_replace_missing_card(self):
        deck = Deck()
        deck.pop_card()
        deck.replace_card(Card(3,13))
        self.assertEqual(deck.cards[52], "13 of Spades", "comparing original card list with replaced card list after using replace method")

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


class TestSong(unittest.TestCase):
    #does it show one instance of class song_dictionary
    def test_one_instance(self):
        asong = show_song()
        self.assertIsInstance(asong,Song, "is asong an instance of class Song")

    def test_search_in_song(self):
        asong2 = show_song("The Hardest Thing")
        self.assertTrue("The Hardest Thing" in str(asong2))








if __name__ == '__main__': #only runs if you call this direct program
    unittest.main(verbosity=2)
