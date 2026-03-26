
class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def __str__(self):
        return f'{self.name} from {self.residence}'

    def __repr__(self):
        return f'Person("{self.name}", "{self.residence}")'

    def tell(self):
        print('I am {} and I live in {}'.format(self.name, self.residence))

    def move(self, new_residence):
        self.residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, customer_number):
        super().__init__(name, residence)
        self.customer_number = customer_number

    def tell(self):
        print('I am VIP customer. My name is {} ({})'.format(self.name,
                                                             self.customer_number))


# -------------------------

p1 = Person('Peter', 'Lhee')
p2 = Customer('Albert', 'Amsterdam', 'VIP007')

p1.tell()
p1.move('Eindhoven')
p1.tell()

p2.tell()

print(str(p1))
print(repr(p1))