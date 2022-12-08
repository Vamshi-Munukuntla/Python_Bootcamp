class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} is deposited in {self.name}'s bank account.")

        else:
            print("Insufficient amount")
            print(f"Balance is ${self.balance}")

        self.show_balance()

    def withdraw(self, amount):
        if amount < 0:
            print('Insufficient funds')
        elif amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f"${amount} is withdrawn from {self.name}'s bank account")

        self.show_balance()

    def show_balance(self):
        print(f"Balance is ${self.balance}")


new_bank_account = BankAccount('Vamshi', 0)
# print(new_bank_account.name)
# print(new_bank_account.balance)
# new_bank_account.deposit(10000)
# new_bank_account.deposit(2000)
# print(new_bank_account.balance)
# new_bank_account.withdraw(-10)
# new_bank_account.withdraw(1000000000)
# new_bank_account.withdraw(1000)
print(type(new_bank_account))
print(isinstance(new_bank_account, BankAccount))
