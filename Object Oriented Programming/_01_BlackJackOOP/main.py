from game import Game
from deck import Deck
from hand import Hand
from money import Money
import sys

print('Welcome to BlackJack')
money = Money(amount=5000)
print(money.amount)
while True:
    # Check if player run out of money
    if money.amount <= 0:
        print("It is good that you weren't playing with real money.")
        print('Thanks for playing')
        sys.exit()

    # Ask player to enter their bet
    print("Money:", money.amount)
    # Get bet
    bet = money.get_bet(max_bet=money.amount)
    # Get Deck
    deck = Deck()
    deck.shuffle()
    # Give the dealer and player two cards from the deck
    dealer_hand = Hand(dealer=True)
    player_hand = Hand()
    for i in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    print('Bet:', bet)
    # Handle player actions
    while True:
        dealer_hand.display()
        player_hand.display()
        print()
        # Check if player has bust
        if player_hand.get_value() > 21:
            break
        # Get player's move
        game = Game()
        move = game.get_move(player_hand.get_value(), money.amount - bet)
        # Handle player moves
        if move == 'D':
            additional_bet = money.get_bet(min(bet, (money.amount - bet)))
            bet += additional_bet
            print(f'Bet increased to {bet}.')
            print('Bet:', bet)
        if move in ("H", "D"):
            # Get another card
            new_card = deck.deal()
            rank = new_card.get_rank()
            suit = new_card.get_suit()
            print(f'You drew a {rank} of {suit}.')
            player_hand.add_card(new_card)
            # Check if player has bust
            if player_hand.get_value() > 21:
                continue
        if move == 'S':
            # Stops players' turn
            break
    # Handle dealers' actions
    if player_hand.get_value() <= 21:
        while dealer_hand.get_value() < 17:
            print('The dealer hits...')
            dealer_hand.add_card(deck.deal())
            dealer_hand.display()
            player_hand.display()
            if dealer_hand.get_value() > 21:
                break
            input("Press enter to continue")
            print('\n\n')
    # Handle whether the player won, lost or draw
    dealer_hand.display(show_dealer=True)
    player_hand.display()
    dealer_value = dealer_hand.get_value()
    player_value = player_hand.get_value()
    if dealer_value > 21:
        print(f'Dealer busts! You win ${bet}!')
        money.add_money(bet)
    elif player_value > 21 or player_value < dealer_value:
        print(f"You lost!")
        money.sub_money(bet)
    elif player_value > dealer_value:
        print(f'You win ${bet}!')
        money.add_money(bet)
    elif player_value == dealer_value:
        print('It is a draw and the bet is returned to you!')
        input('Press enter to continue...')
        print('\n\n')












