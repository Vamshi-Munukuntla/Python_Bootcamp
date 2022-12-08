from deck import BACKSIDE


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        "Return value of cards."
        value = 0
        number_aces = 0
        # Add the value for non ace cards.
        for card in self.cards:
            rank = card.get_rank()
            if rank == "A":
                number_aces += 1
            elif rank in ('K', 'J', 'Q'):
                value += 10
            else:
                value += int(rank)
        value += number_aces
        for i in range(number_aces):
            # If another 10 can be added without busting
            if value + 10 <= 21:
                value += 10
        self.value = value
        return self.value

    def display_card_image(self, cards):
        """Display all the cards in the card list"""
        rows = ['', '', '', '', '']
        for card in cards:
            rows[0] += ' ___  '
            if card == BACKSIDE:
                rows[1] += '|## | '
                rows[2] += '|###| '
                rows[3] += '|_##| '
            else:
                rank, suit = card.get_rank(), card.get_suit()
                rows[1] += '|{} | '.format(rank.ljust(2))
                rows[2] += '| {} | '.format(suit)
                rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
        for row in rows:
            print(row)

    def display(self, show_dealer=False):
        """Show player's and dealer's hand"""
        if self.dealer and show_dealer == False:
            print("DEALER: ???")
            # Hide dealer's first card
            self.display_card_image([BACKSIDE] + self.cards[1:])
        # Show the player's cards
        elif self.dealer and show_dealer:
            print("DEALER:", self.get_value())
            self.display_card_image(self.cards)
        else:
            print("PLAYER:", self.get_value())
            self.display_card_image(self.cards)
