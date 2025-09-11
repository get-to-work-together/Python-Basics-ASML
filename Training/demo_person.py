
class Person:
    """This is my Person class"""

    def __init__(self, name, residence):
        self._name = name.upper()
        self._residence = residence

    def __repr__(self):
        return f"Person('{self._name}', '{self._residence}')"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name.upper()

    def tell_me_something(self):
        """Print information"""
        print(f'I am {self._name} and I live in {self._residence}')

    def move(self, new_residence):
        """Change the attribute residence"""
        print(f'Moving to {new_residence}')
        self._residence = new_residence


# -------------------

if __name__ == '__main__':

    p1 = Person('Peter', 'Lhee')   # instantiation
    p2 = Person('Jan', 'Eindhoven')   # instantiation

    p1.tell_me_something()
    p2.tell_me_something()

    p1.move('Amsterdam')

    p1.tell_me_something()

    print(p1)
    print(p2)

    print(p1.get_name())
    p1.set_name('Hacked')
    print(p1.get_name())
