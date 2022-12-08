from card import Card
import random

HEARTS = chr(9829)  # Character is '♥'
DIAMONDS = chr(9830)  # Character is  '♦'
SPADES = chr(9824)  # Character is  '♠'
CLUBS = chr(9827)  # Character is  '♣'
BACKSIDE = 'backside'


class Deck:
    def __init__(self):
        """Return a list of tuples (rank , suit) for all 52 cards"""
        self.cards = []
        for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
            for rank in range(2, 11):
                # add the numbered cards
                self.cards.append(Card(suit, str(rank)))
            for rank in ('J', 'Q', "K", "A"):
                # add face and ace cards
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)
