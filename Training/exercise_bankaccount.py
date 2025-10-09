
class BankAccount:
    """This in my BankAccount class"""

    __slots__ = ('__holder', '__accountnr', '__balance')

    currency = '$'

    def __init__(self, holder, accountnr, balance=0.0):
        self.__holder = holder
        self.__accountnr = accountnr
        self.__balance = balance

    def info(self):
        """Return account information"""
        return f'Account nr {self.__accountnr} belongs to {self.__holder} and has a balance of {BankAccount.currency}{self.__balance:.2f}.'

    def deposit(self, amount):
        """Add amount to balance"""
        self.__balance += amount

    def withdraw(self, amount):
        """Subtract amount to balance"""
        self.__balance -= amount


# -------------------------------------------------------------

acc1 = BankAccount('Peter', 'NL99ABCD0976545361', 200)
acc2 = BankAccount('Jan', 'NL99ABCD0976545362')

print(acc1.info())

acc1.deposit(2000)
acc1.withdraw(121)
acc1.withdraw(45)
acc1.withdraw(300)

print(acc1.info())

print(help(BankAccount))

