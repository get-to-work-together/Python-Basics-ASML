import bankaccount

acc1 = bankaccount.BankAccount('NL99ABCD0123487654', 'Peter')

acc1.info()

acc1.deposit(1000)
acc1.withdraw(100)
acc1.withdraw(121)
acc1.deposit(1000)
acc1.withdraw(300)

acc1.info()
