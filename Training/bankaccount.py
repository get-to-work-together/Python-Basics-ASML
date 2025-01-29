from datetime import datetime

class BankAccount:
    """This is my superb bank account class. Written by Peter."""

    # initialize attributes here
    def __init__(self, accountnr: str, holder: str, balance: float|int = 0.0):
        self._accountnr = accountnr
        self._holder = holder
        self._balance = balance
        self._transitions = []

    # methods
    def deposit(self, amount: float|int):
        """My deposit method. Make sure the amount is positive."""
        if amount < 0:
            raise Exception('Amount must be positive.')
        self._transitions.append((datetime.now(), 'deposit', amount))
        self._balance += amount

    def withdraw(self, amount: float|int):
        """My withdraw method. Make sure the amount is positive."""
        if amount < 0:
            raise Exception('Amount must be positive.')
        self._transitions.append((datetime.now(), 'withdraw', amount))
        self._balance -= amount

    def info(self):
        print(f'Bankaccount nr {self._accountnr} belangs to {self._holder} has a balance of €{self._balance}.')

    def print_transitions(self):
        for transition in self._transitions:
            print(transition)

# ----------------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL99ABCD0123487654', 'Jan', 1000)

    acc1.info()

    acc1.deposit(1000)
    acc1.withdraw(100)
    acc1.withdraw(121)
    acc1.deposit(1000)
    acc1.withdraw(300000)

    acc1.info()

    acc1.print_transitions()

