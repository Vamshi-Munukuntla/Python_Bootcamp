import sys


class Game:
    def __init__(self):
        pass

    def get_move(self, player_hand, money):
        """Ask the player for their move, return H , S or D"""
        while True:
            # Determine what move the player can make
            moves = ["(H)it", "(S)tand"]
            if len(str(player_hand)) == 2 and money > 0:
                moves.append('(D)ouble down')
            # Ask from player the move, by showing options
            move_prompt = ', '.join(moves) + '>'
            move = input(move_prompt).upper()
            if move in ('H', 'S'):
                return move
            if move == 'D' and '(D)ouble down' in moves:
                return move

