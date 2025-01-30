
class Person:

    # initialization attributes
    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    # methods
    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, customernr):
        super().__init__(name, residence)
        self.customernr = customernr

    def tell(self):
        print(f'I am a customer. My name is {self.name}. My number is {self.customernr}.')


# ----------------------------------------

p1 = Person('Peter', 'Lhee')   # instantiation => __init__ magic method
p2 = Person('Janneke', 'Amsterdam')
p3 = Customer('Kim', 'Delft', 'VIP982')

print(type(p1))

p1.tell()    # Python translates this to => Person.tell(p1)

p1.move('Eindhoven')   # Python translates this to => Person.move(p1, new_residence)

p1.tell()
p2.tell()
p3.tell()
