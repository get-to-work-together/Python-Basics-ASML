class BankAccount:

    def __init__(self, holder: str, accountnr: str, balance: int|float = 0.0):
        self._holder = holder
        self._accountnr = accountnr
        self._balance = float(balance)

    def deposit(self, amount: int|float):
        self._balance = round(self._balance + float(amount), 2)

    def withdraw(self, amount: int|float):
        if amount > self._balance:
            raise Exception('Not enough funds!!')
        self._balance = round(self._balance - float(amount), 2)

    def info(self):
        return f'Account {self._accountnr} belongs to {self._holder} and has a balance of €{self._balance:.2f}'


# -------------

if __name__ == '__main__':
    acc1 = BankAccount('Peter', 'NL99ABCD0234532419', '100')
