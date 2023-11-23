class BankAccount:
    def __init__(self):
        self.balance = 1000

    def deposit(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 2

    def deposit(self):
        self.balance += self.balance*0.003
        print(self.balance)


SavingsAccount().deposit()