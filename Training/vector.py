
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'[{self._x}, {self._y}]'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __eq__(self, other):
        return self.length() == other.length()

    def __ne__(self, other):
        return self.length() != other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5


# --------------

v1 = Vector(6, 7)
v2 = Vector(4, -5)

print(v1)
print(v2)

v3 = v1 + v2

print(v3)

print(v1.length())
print(v2.length())
print(v3.length())

if v1 > v2:
    print('v1 is longer than v2')
elif v2 > v1:
    print('v2 is longer than v1')
else:
    print('v1 and v2 are just as long')
