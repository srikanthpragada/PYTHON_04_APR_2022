class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f"Balance is {self.balance}, but withdraw amount is {self.amount}"


class Account:
    # Static/class variable/attribute
    minbal = 5000

    @staticmethod
    def getMinbal():
        return Account.minbal

    def __init__(self, acno, customer, balance=0):
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise InsufficientFundsError(amount=amount, balance=self.balance)

    def getBalance(self):
        return self.balance


print('Minbal', Account.getMinbal())

a = Account(1, "Randy", 20000)
a.deposit(10000)
print(a.getBalance())
a.withdraw(50000)
