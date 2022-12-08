class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_pay(self):
        return self.salary


class SalesEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name=name, salary=salary)
        self.sales_bonus = 0

    def calculate_bonus(self, items):
        self.sales_bonus = 200*items

    def get_pay(self):
        return self.salary + self.sales_bonus


new_sales_employee = SalesEmployee('Re', 1000)
print(new_sales_employee.get_pay())
new_sales_employee.calculate_bonus(10)
print(new_sales_employee.get_pay())
