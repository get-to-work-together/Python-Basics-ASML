import logging

logging.basicConfig(
    filename = 'example.log', # or to a file 'example.log',
    level = logging.INFO,
    format = '%(asctime)s.%(msecs)03d - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S')

class BankAccount:

    def __init__(self, number, holder, balance = 0):
        self._number = number
        self._holder = holder
        self._balance = balance

    def withdraw(self, amount):
        logging.info(f'Withdraw of {amount}')
        self._balance -= amount

    def deposit(self, amount):
        logging.info(f'Deposit of {amount}')
        self._balance += amount

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a balance of €{self._balance}.'

    @staticmethod
    def ask(acc):
        while True:
            action = input('What do you want to do? [(d)eposit, (w)ithdraw, (i)nfo, (q)uit]:')

            if action.startswith('d'):
                amount = float(input('How much do you want to deposit? : '))
                acc.deposit((amount))
            elif action.startswith('w'):
                amount = float(input('How much do you want to withdraw? : '))
                acc.withdraw((amount))
            elif action.startswith('i'):
                print(acc.get_info())
            elif action.startswith('q'):
                break


# ---------------------------------------------------------

if __name__ == '__main__':

    acc = BankAccount('NL23ABCD0345673456', 'Peter')

    # BankAccount.ask(acc)

    acc.deposit(1000)
    acc.withdraw(245)
    acc.withdraw(34)