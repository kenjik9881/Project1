SI 507 Project 1 - Read Me File

~~What is this?~

This project includes code that replicates some actions that you can take with a real deck of cards.
The code specifies two classes, class Card and class Deck.

class Card aims to output a card in the form of "Ace of Spades" or "King of Hearts". Currently there is a bug
so that you will see "13 of Hearts" instead of "King of Hearts". The code is supposed to take in information
regarding the suit, the rank of the card (from 1-13), and also if it is a face card and then should output
that card in a nice format of "King of Hearts." This bug is still being fixed.

class Deck first will build a deck of a list of cards. This list will contain all of the 52 cards in a normal
playing card deck. So, this deck will consist of the four suits with all cards from 1-13 in those suits.

class Deck has several methods which aim to several things. These methods are listed here.

string method - This will return a multi-line string with all of the cards in a deck.

pop_card method - This method allows you to remove one card at a time from the top of the deck. If you invoke this method, 52 times, then you will no longer have any cards left in your deck.

shuffle method - This method works like a shuffler in real life. If you run it on the deck of cards, it will shuffle
your deck into a random order.

sort_cards method - This method will sort any cards in the deck. It sorts it by ascending order by suit: Diamonds, then Clubs, then Hearts, then Spades.

replace_card method - This method will replace a card into the deck if it is not in the deck (for example if it has previously been removed using the pop_card method).

deal_hand method - This method aims to take an inputted hand size from the user (for example 5) and then will deal out that size of hand. There is a known bug with this method that if the inputted hand size is too large (for example if you try to deal the whole deck), then an IndexError will be raised.

The code also contains two functions: play_war_game and show_song

The play_war_game function mimics the popular two-player card game, War. War allows two players to compare each card, card by card. The player who has the higher card (for example a Jack versus a 10) will be given a point. There is no input required for this function. A winner will be declared once 52 cards have been played.

The show_song is a fun function that aims to take a string as input to use as a search term for songs on iTunes. You should be able to search for any song but there is a bug which causes it to only search for songs that have "win","winner","hurrah", or "hooray" in the song title.

~ Is the code ready? ~
The code is almost there. There are three bugs identified as mentioned earlier. These bugs are:
* a bug with the string method in class Card
* a bug with the deal_hand method in class Deck
* a bug with the show_song function that doesn't actually search the iTunes API for any user-inputted information but rather picks randomly from four search terms.

~ How do I access this code and make clone of my own? ~
You can access it here: https://github.com/kenjik9881/Project1
From here simply click on the 'Fork' button to create your own clone of this code.
The code file is SI507F17_project1_cards.py
This code uses Python 3.6

~ What packages or libraries do I need? ~
All the necessary packages to run this code are listed in the 'requirements.txt' file. This file is available on https://github.com/kenjik9881/Project1

~ Where are the tests? ~
The tests are also accessible on this link:https://github.com/kenjik9881/Project1
The test file is SI507F17_project1_tests.py
