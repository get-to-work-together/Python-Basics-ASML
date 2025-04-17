
class BankAccount:
    currency = '$'

    def __init__(self, accountnr, holder, balance = 0):
        self._accountnr = accountnr
        self._holder = holder
        self._balance = float(balance)

    def __str__(self):
        return f'Account {self._accountnr} from {self._holder} Balance: {BankAccount.currency}{self._balance:.2f}.'

    def __repr__(self):
        return f'BankAccount( {self._accountnr}, {self._holder}, {self._balance:.2f})'

    def info(self):
        print(f'Account with number {self._accountnr} from {self._holder} has a balance of {BankAccount.currency}{self._balance:.2f}.')

    def deposit(self, amount):
        self._balance += amount
        self.info()

    def withdraw(self, amount):
        if amount > self._balance:
            raise Exception('Not enough funds!')
        self._balance -= amount
        self.info()


# -------------------------------------------------------

if __name__ == '__main__':

    acc = BankAccount('NL1234ABCD0278364388', 'Peter', 100)

    acc.info()

    try:
        acc.deposit(1000)
        acc.withdraw(100)
        acc.withdraw(10000)

    except Exception as ex:
        print(ex)

    print(str(acc))
    print(repr(acc))
