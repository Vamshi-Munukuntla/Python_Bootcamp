class Person:
    def __init__(self):
        self.phone_number = 0

    def update_contact(self, new_number):
        self.phone_number = new_number
        print(f"Phone number has been updated to {self.phone_number}")


class Customer(Person):
    def __init__(self):
        super().__init__()

    def purchase(self, item):
        print(f"{item} has been purchased")


new_customer = Customer()
new_customer.purchase('Coffee')
print(new_customer.phone_number)
new_customer.update_contact(5656)

