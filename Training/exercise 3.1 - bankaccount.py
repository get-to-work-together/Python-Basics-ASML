
class Bankaccount(object):

    currency = '$'

    __slots__ = ('_accountnr', '_holder', '_balance')

    def __init__(self, accountnr, holder, balance = 0.0):
        self._accountnr = accountnr
        self._holder = holder
        self._balance = balance

    def __repr__(self):
        return f'Bankaccount("{self._accountnr}", "{self._holder}", {self._balance})'

    def __str__(self):
        return f'Account nr {self._accountnr} belongs to {self._holder} has a balance of {Bankaccount.currency} {self._balance:.2f}.'

    def __add__(self, other):
        return self._balance + other._balance

    def __eq__(self, other):
        return self._balance == other._balance
    def __ne__(self, other):
        return self._balance != other._balance
    def __lt__(self, other):
        return self._balance < other._balance
    def __le__(self, other):
        return self._balance <= other._balance
    def __gt__(self, other):
        return self._balance > other._balance
    def __ge__(self, other):
        return self._balance >= other._balance


    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise Exception('Insufficient funds!')
        self._balance -= amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def info(self):
        print( f'Account nr {self._accountnr} belongs to {self._holder} has a balance of {Bankaccount.currency} {self._balance:.2f}.' )


# -----------------------------------------------------------------------------

acc1 = Bankaccount('NL99ABCD01234543212', 'Peter')
acc2 = Bankaccount('NL98ABCD01234888888', 'Yen', 100)

acc1.info()
acc2.info()

acc1.deposit(123)
acc2.withdraw(12)
acc2.deposit(1000)
acc1.withdraw(34)
acc2.deposit(50)
acc1.deposit(300)

acc1.info()
acc2.info()

acc1.transfer(acc2, 99)

acc1.withdraw(100)

acc1.info()
acc2.info()

print(repr(acc1))
print(str(acc1))

print(acc1 + acc2)

print(acc1 < acc2)

accounts = [acc1, acc2, Bankaccount('123','Me',10020), Bankaccount('67','You',10)]

for acc in sorted(accounts):
    print(acc)