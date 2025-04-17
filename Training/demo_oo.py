
class Person:

    __slots__ = ['name', 'residence']

    def __init__(self, name: str, residence: str = 'Unknown'):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence


# ------------------------------

p = Person('Peter')

p.tell()
p.move('Amsterdam')
p.tell()   # => Person.tell(p)