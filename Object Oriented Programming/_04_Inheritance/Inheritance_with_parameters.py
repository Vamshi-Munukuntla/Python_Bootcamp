import random
class Person:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def update_contact(self, new_number):
        self.phone_number = new_number
        print(f"Phone number has been updated to {self.phone_number}")


class Customer(Person):
    def __init__(self, name, phone_number, address):
        super().__init__(name=name,
                         phone_number=phone_number,
                         address=address)
        self.customer_id = random.randint(1, 100)
        self.email_id = "-"

    def purchase(self, item):
        print(f"{item} has been purchased.")


new_customer = Customer('Vamshi', '111', '1-near land')
print(new_customer.phone_number)
new_customer.update_contact(5689)
new_customer.purchase('Tea & Coffee')
print(new_customer.customer_id)
print(new_customer.email_id)
