
class Person:

    __slots__ = ['name', 'residence']

    def __init__(self, name, residence = 'unknown'):
        # attributes
        self.name = name
        self.residence = residence

    # methods
    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence


class Customer(Person):

    def __init__(self, name, residence = 'unknown', customernr = 'unknown'):
        # attributes
        super().__init__(name, residence)
        self.customernr = customernr

    def tell(self):
        print(f'I am a VIP customer. My name is {self.name}. Nr.: {self.customernr}')


# -----------------------------------

# objects / instances
p1 = Person('Peter')
p2 = Customer('Jochem', 'Nieuwegein', 'VIP007')

p1.tell()
p2.tell()

p2.move('Almelo')
p2.tell()
