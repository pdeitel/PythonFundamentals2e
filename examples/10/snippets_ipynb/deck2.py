# deck.py
"""Deck class represents a deck of Cards."""
import random
from carddataclass import Card

class DeckOfCards:
    NUMBER_OF_CARDS: int = 52 # constant number of Cards

    def __init__(self) -> None:
        """Initialize the deck."""
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13],
                Card.SUITS[count // 13]))

    def shuffle(self) -> None:
        """Shuffle deck."""
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self) -> Card | None:
        """Return one Card."""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except IndexError:
            return None

    def __str__(self) -> str:
        """Return a string representation of the current _deck."""
        deck_string = ''

        for index, card in enumerate(self._deck):
            deck_string += f'{card:<19}'
            if (index + 1) % 4 == 0:
                deck_string += '\n'

        return deck_string

##########################################################################
# (C) Copyright 1992-2026 by Deitel & Associates, Inc. and               #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
