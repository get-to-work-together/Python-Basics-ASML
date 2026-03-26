import math
from abc import ABC, abstractmethod


class AbstractVector(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass


class Vector(AbstractVector):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return '[{}, {}]'.format(self._x, self._y)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __iter__(self):
        self.attributes = ['_x', '_y']
        self.i = -1
        return self

    def __next__(self):
        current_index = self.i
        self.i += 1
        if self.i >= len(self.attributes):
            raise StopIteration
        current_attribute = self.attributes[current_index]
        return current_attribute, getattr(self, current_attribute)

    def length(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __gt__(self, other):
        return self.length() > other.length()
    def __ge__(self, other):
        return self.length() >= other.length()
    def __lt__(self, other):
        return self.length() < other.length()
    def __le__(self, other):
        return self.length() <= other.length()
    def __eq__(self, other):
        return self.length() == other.length()
    def __ne__(self, other):
        return self.length() != other.length()

# --------------------------------

if __name__ == '__main__':

    v1 = Vector(3, 4)
    v2 = Vector(5, 6)

    print(v1)
    print(v2)

    v3 = v1 + v2
    print(v3)

    print(v1.length())
    print(v2.length())
    print(v3.length())

    if v1 > v2:
        print('v1 is longer than v1')
    else:
        print('v1 is shorted than v2')

    for attr, value in v1:
        print(attr, value)
