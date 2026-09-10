
class Bankaccount:

    __slots__ = ('_holder', '_nr', '_balance')

    # class-wide attribute
    currency = '\u20AC'  # €

    def __init__(self,
                 holder: str,
                 nr: str,
                 balance: int|float = 0.0):
        self._holder = holder
        self._nr = nr
        self._balance = float(balance)

    def deposit(self, amount: int|float):
        self._balance += amount

    def withdraw(self, amount: int|float):
        self._balance -= amount

    def info(self) -> str:
        return f'Account {self._nr} belongs to {self._holder} and has a balance of {Bankaccount.currency}{self._balance:.2f}'

    @staticmethod
    def calculate_interest(amount, interest_percentage):
        return amount * interest_percentage / 100

    def add_interest(self, interest_percentage = 5):
        interest = Bankaccount.calculate_interest(self._balance, interest_percentage)
        self._balance += interest

# -----------------------------------------------------

if __name__ == '__main__':

    account1 = Bankaccount('Peter', 'NL99ABCD0123454321')

    print(account1.info())

    account1.deposit(1000)
    account1.withdraw(121.50)
    account1.withdraw(99)
    account1.withdraw(200)
    account1.deposit(1000)

    print(account1.info())

    account1.add_interest()

    print(account1.info())
