
class Person:

    # initialize
    def __init__(self, name: str, residence: str = 'Unknown'):
        self.name = name
        self.residence = residence

    # methods
    def tell(self) -> str:
        return f'I am {self.name} and I live in {self.residence}'

    def move(self, new_residence: str):
        if new_residence == '':
            raise Exception('Empty residence not allowed')
        self.residence = new_residence

class Bing:
    counter = 0
    def say_bing(self):
        Bing.counter += 1
        print('BING!!!!!', Bing.counter)

class Customer(Person, Bing):
    def __init__(self, name: str, residence: str = 'Unknown', customernr: str = 'unknown'):
        super().__init__(name, residence)
        self.customernr = customernr

    def tell(self) -> str:
        return f'I am a VIP customer {self.name}!!!! My customer number is {self.customernr}.'


# ------------------------------------------

p1 = Person('Peter', 'Lhee')
p2 = Customer('Richard', 'Helmond', 'VIP007')

print(p1.tell())     # => Person.tell(p)
p1.move('Eindhoven')
print(p1.tell())

print(p2.tell())

p2.say_bing()
p2.say_bing()
p2.say_bing()
p2.say_bing()
p2.say_bing()
