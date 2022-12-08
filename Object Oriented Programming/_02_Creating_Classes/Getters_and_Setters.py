# class Customer:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, balance):
#         if balance < 0:
#             self.__balance = 0
#         elif balance > 10000:
#             self.__balance = 0
#         else:
#             self.__balance = balance

class Customer:

    def __init__(self, name, balance):
        self.name = name
        self.__set_balance(balance)

    def __get_balance(self):
        return self.__balance

    def __set_balance(self, balance):
        if balance < 0:
            self.__balance = 0
        elif balance > 10000:
            self.__balance = 10000
        else:
            self.__balance = balance

    balance = property(__get_balance, __set_balance)


c1 = Customer('vamshi', 10)
print(c1.balance)
# print(c1.get_balance())
c1.balance = 100
print(c1.balance)
