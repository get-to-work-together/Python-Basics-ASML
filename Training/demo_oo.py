
class Person:
    """My Person class"""

    def __init__(self, name: str, residence: str = 'Unknown') -> None:
        """Initialize Person class"""
        self.name = name
        self.residence = residence

    def tell(self) -> None:
        "Print name and residence info"
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence: str) -> None:
        """Change residence to new residence"""
        print(f'I moved to {new_residence}.')
        self.residence = new_residence


class Customer(Person):
    """My Customer class"""

    def __init__(self, name: str, residence: str = 'Unknown', customernr='') -> None:
        super().__init__(name, residence)
        self.customernr = customernr

    def tell(self) -> None:
        "Print name and residence info"
        print(f'I am a VIP customer. My name is {self.name}. My number is {self.customernr}.')


# -----------------------------------------

p1 = Person('Peter')    # instatiation

p1.tell()    # => Person.tell(p1)
p1.move('Eindhoven')
p1.tell()    # => Person.tell(p1)

p2 = Customer('Lionel', residence = 'Eindhoven', customernr='VIP0007')    # instatiation

p2.tell()
