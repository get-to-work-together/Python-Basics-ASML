
class Person(object):

    __slots__ = ('_name', '_residence')

    def __init__(self, name: str, residence: str):
        self._name = name
        self._residence = residence

    def __repr__(self):
        return f'Person object with name: {self._name}.'

    def tell(self):
        print(f'I am {self._name} and I live in {self._residence}.')

    def move(self, new_residence: str):
        self._residence = new_residence


class Customer(Person):

    def __init__(self, name: str, residence: str, customernr: str):
        super().__init__(name, residence)
        self._customernr = customernr

    def __repr__(self):
        return f'Customer object with name: {self._name}.'

    def tell(self):
        print(f'I am a customer {self._customernr} and my name is {self._name}.')

# ---------------------------------------

p = Customer('Peter', 'Lhee', 'VIP000233')   # instantiation

print(type(p))
print(p)
print(dir(p))

p.tell()
Person.tell(p)

p.move('Eindhoven')

p.tell()
