class Money:
    def __init__(self, amount):
        self.amount = amount

    def add_money(self, amount):
        self.amount += amount

    def sub_money(self, amount):
        self.amount -= amount

    def get_bet(self,max_bet):
        """Ask the player how much money they want to bet for this round"""
        while True:
            print("How much do you bet? (1-{}, or QUIT)".format(max_bet))
            bet = input('> ').upper().strip()
            if bet == 'QUIT':
                print("Thanks for playing!")
                sys.exit()
            if not bet.isdecimal():
                continue
            bet = int(bet)
            if 1 <= bet <= max_bet:
                return bet