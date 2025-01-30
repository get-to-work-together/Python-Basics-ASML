
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._length = (self._x ** 2 + self._y ** 2) ** 0.5

    def __repr__(self):
        return f'[{self._x}, {self._y}]'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __gt__(self, other):
        return self._length > other._length

    def __ge__(self, other):
        return self._length >= other._length

    def __lt__(self, other):
        return self._length < other._length

    def __le__(self, other):
        return self._length <= other._length

    def __eq__(self, other):
        return self._length == other._length

    def __ne__(self, other):
        return self._length != other._length

    @property
    def length(self):
        return self._length

# --------

v1 = Vector(10, 10)
v2 = Vector(8, -6)

print(v1)
print(v2)

v3 = v1 + v2

print(v3)

print(v1.length)
print(v2.length)

print(v1 > v2)
print(v1 >= v2)
print(v1 < v2)
print(v1 <= v2)

