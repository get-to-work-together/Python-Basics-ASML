
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return '[%g, %g]' % (self._x, self._y)

    def __repr__(self):
        return '[%g, %g]' % (self._x, self._y)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def __eq__(self, other):
        return self.length() == other.length()
    def __ne__(self, other):
        return self.length() != other.length()
    def __lt__(self, other):
        return self.length() < other.length()
    def __le__(self, other):
        return self.length() <= other.length()
    def __gt__(self, other):
        return self.length() > other.length()
    def __ge__(self, other):
        return self.length() >= other.length()


# -----------------------------------------------------------

v1 = Vector(5, 8)
v2 = Vector(3, -2)

print(v1)
print(v2)

v3 = v1 + v2

print(v3)

print(v1.length())
print(v2.length())
print(v3.length())

print(sorted([v1, v2, v3]))
