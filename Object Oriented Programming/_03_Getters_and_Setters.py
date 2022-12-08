#TODO 1 - Create class for Employees which has two attributes public name and private salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # # TODO 3 - Create getter and setter methods to access and update salary
    # def __get_salary(self):
    #     return self.__salary
    #
    # def __set_salary(self, new_salary):
    #     self.__salary = new_salary
    #
    # # TODO 4 - Change getter and setter methods using property
    # salary = property(__get_salary, __set_salary)

    # TODO 5 - Change them in Pythonic way using decorators
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < self.__salary:
            print("The salary cannot be decreased")
        else:
            self.__salary = new_salary


# TODO 2 - Create two different employee objects based on Employee class
employee1 = Employee("Elshad", 1000)
employee2 = Employee("Renad", 1500)
print(employee1.name)
print(employee1.salary)
employee1.salary = 1200
print(employee1.salary)


