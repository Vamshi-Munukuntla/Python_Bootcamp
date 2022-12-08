class Customer:

    def __init__(self, name, balance, contact_num):
        self.name = name
        self.__balance = balance
        self.__contact_num = contact_num

    def display_details(self):
        print(f"Name: {self.name}, Contract Number: {self.contact_num}")

    def display_balance(self):
        print(f"{self.name}'s outstanding balance is ${self.balance}")


customer1 = Customer("Vamshi", 1000000, 9701311671)
print(customer1._Customer__contact_num)
print(customer1._Customer__balance)