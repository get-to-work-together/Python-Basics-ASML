from dataclasses import dataclass


@dataclass
class BankAccount:
    holder: str
    accountnr: str
    balance: float = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def info(self):
        print('Account {} belonging to {} has a balance of € {}'.format(self.accountnr,
                                                                        self.holder,
                                                                        self.balance))


# ---------------------------------------------------

acc1 = BankAccount('Peter', 'NL99ABCD01234865432')
acc1.info()

acc1.deposit(1000)
acc1.withdraw(100)
acc1.withdraw(21)
acc1.withdraw(200)
acc1.info()
