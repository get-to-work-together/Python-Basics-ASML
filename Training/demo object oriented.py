
class Person:

    # special method
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
        print(f'I am {self.name} and I am a VIP customer. My customernr is {self.customernr}')



# ===========================


p = Person('Peter', 'Lhee')

p.tell()
p.move('Eindhoven')
p.tell()

c = Customer('Alice', 'Veldhoven', 'VIP007')

c.tell()
