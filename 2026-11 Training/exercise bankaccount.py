
class Bankaccount:
    _currency = '$'

    def __init__(self, holder, nr, balance = 0.0):
        self._holder = holder
        self._nr = nr
        self._balance = float(balance)

    def deposit(self, amount):
        self._balance = round(self._balance + amount, 2)

    def withdraw(self, amount):
        self._balance = round(self._balance - amount, 2)

    def info(self):
        return f'Account {self._nr} belongs to {self._holder} and has a balance of {Bankaccount._currency}{self._balance:.2f}'

    @staticmethod
    def change_currency(currency='€'):
        Bankaccount._currency = currency


# -----------------------------------------------------

if __name__ == '__main__':

    account1 = Bankaccount('Peter', 'NL99ABCD0123454321')
    Bankaccount.change_currency('EUR')

    print(account1.info())

    account1.deposit(1000)
    account1.withdraw(121.50)
    account1.withdraw(99)
    account1.withdraw(200)
    account1.deposit(1000)
    account1.deposit(0.1)
    account1.deposit(0.2)


    print(account1.info())
