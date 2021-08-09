class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise NotImplemented

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return f'User {self.name} with balance: {self.balance}'
