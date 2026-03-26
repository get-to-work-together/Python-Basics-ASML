
class BankAccount:

    currency = '$'

    def __init__(self, holder, accountnr, balance = 0.0):
        self._holder = holder
        self._accountnr = accountnr
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def info(self):
        print('Account {} belonging to {} has a balance of {} {}'.format(self._accountnr,
                                                                         self._holder,
                                                                         BankAccount.currency,
                                                                         self._balance))


# ---------------------------------------------------

acc1 = BankAccount('Peter', 'NL99ABCD01234865432')
acc1.info()

# print(dir(acc1))

acc1.deposit(10)
acc1.withdraw(20)

acc1.deposit(1000)
acc1.withdraw(100)
acc1.withdraw(21)
acc1.withdraw(200)
acc1.info()
