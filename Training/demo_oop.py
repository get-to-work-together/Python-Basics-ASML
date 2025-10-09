
class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence


class Client(Person):

    def tell(self):
        print(f'I a client and my name is {self.name} and I live in {self.residence}.')


# -------------------------------------

p = Client('Peter', 'Lhee')        # instantiation

p.tell()
p.move('Eindhoven')
p.tell()
