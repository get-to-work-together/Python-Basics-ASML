
class Person:

    # initialize attributes
    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    # methods
    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, customer_number):
        super().__init__(name, residence)
        self.customer_number = customer_number

    def tell(self):
        print(f'I am a VIP customer. My name is {self.name} and customer number is {self.customer_number}.')


# --------------------------------------------------------------------------

# Instantiation
p = Person('Peter', 'Lhee')

# call a methods
p.tell()
p.move('Eindhoven')
p.tell()

c = Customer('Peter', 'Lhee', 'VIP007')

c.tell()
