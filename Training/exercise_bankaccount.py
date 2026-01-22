
class BankAccount:

    __slots__ = ['_holder', '_accountnr', '_balance']

    def __init__(self, holder, accountnr, balance = 0.0):
        self._holder = holder
        self._accountnr = accountnr
        self._balance = balance

    def desposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def info(self):
        print(f'BankAccount - holder="{self._holder}", accountnr="{self._accountnr}", balance=€{self._balance:.2f}')


# ====================================================================

if __name__ == '__main__':

    acc1 = BankAccount('Peter', 'NL00ABCD0123487654')

    acc1.desposit(1000)
    acc1.withdraw(110)
    acc1.info()
