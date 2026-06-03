
from bankaccount import BankAccount

# --------------------------------------------------------------------------

acc1 = BankAccount('Peter', 'NL99ABCD0234532419', '100')

print(acc1.info())

acc1.deposit(1000)
acc1.withdraw(121)
acc1.withdraw(250)
acc1.deposit(0.1)
acc1.deposit(0.2)

print(acc1.info())

try:
    acc1.withdraw(1000000)
except Exception as ex:
    print(ex)