import random


class Person:
    def __init__(self, name, phone="-", address="-", email="-"):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def update_contact(self, new_number):
        self.phone = new_number


class Employee(Person):
    def __init__(self, name, phone, address, email):
        super().__init__(name=name, phone=phone,
                         address=address, email=email)
        self.employee_number = random.randint(500, 5000)

    def promote(self, new_position):
        self.promote = new_position
        print(f"{self.name} is promoted to {self.promote}")

    def retire(self, retire_status):
        self.retire = retire_status
        print(f"Is {self.name} retired? - {self.retire}.")


class Customer(Person):
    def __init__(self, name, phone, address, email):
        super().__init__(name=name, phone=phone,
                         address=address, email=email)
        self.customer_id = random.randint(1, 499)

    def purchase(self, item):
        self.purchase = item
        print(f"{self.name} purchased {self.purchase}")


class Courier(Person):
    def __init__(self, name, phone, address, email):
        super().__init__(name=name, phone=phone,
                         address=address, email=email)

    def deliver_packages(self, number):
        self.deliver_packages = number
        print(f"Number of packages to be delivered today are {self.deliver_packages}.")


new_customer = Person('El shad')
print(new_customer.phone)
print(new_customer.address)
new_customer.email = '@gmail.com'
print(new_customer.email)

new_employee = Employee('Vamshi', '91', '11', '59@gmail.com')
print(new_employee.address)
new_employee.promote('Chef')
new_employee.retire('False')

new_customer1 = Customer('Jane Austen', "--", "--", "--")
print(new_customer1.phone)
print(new_customer1.address)
print(new_customer1.email)
new_customer1.purchase('Coffee and Donut.')

courier_man = Courier('Kunal Shah', "--", "--", "--")
print(courier_man.phone)
print(courier_man.address)
print(courier_man.email)
courier_man.deliver_packages(23)
