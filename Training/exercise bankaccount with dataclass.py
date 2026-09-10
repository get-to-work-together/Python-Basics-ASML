from dataclasses import dataclass

@dataclass
class Bankaccount:
    holder: str
    nr: str
    balance: float = 0.0

    currency = '\u20AC'  # €

    def deposit(self, amount: int|float):
        self.balance += amount

    def withdraw(self, amount: int|float):
        self.balance -= amount

    def transfer(self, other: Bankaccount, amount: int|float):
        if not isinstance(other, Bankaccount):
            raise Exception('Not a Bankaccount instance')
        self.withdraw(amount)
        other.deposit(amount)

    def info(self) -> str:
        return f'Account {self.nr} belongs to {self.holder} and has a balance of {Bankaccount.currency}{self.balance:.2f}'

    @staticmethod
    def calculate_interest(amount, interest_percentage):
        return amount * interest_percentage / 100

    def add_interest(self, interest_percentage = 5):
        interest = Bankaccount.calculate_interest(self.balance, interest_percentage)
        self.balance += interest

# -----------------------------------------------------

if __name__ == '__main__':

    account1 = Bankaccount('Peter', 'NL99ABCD0123454321')
    account2 = Bankaccount('Richard', 'NL99ABCD0123459999')

    print(account1.info())

    account1.deposit(1000)
    account1.withdraw(121.50)
    account1.withdraw(99)
    account1.withdraw(200)
    account1.deposit(1000)

    print(account1.info())

    account1.add_interest()

    print(account1.info())

    print(account1)

    account1.transfer(account2, 876)
    print(account1.info())
    print(account2.info())

