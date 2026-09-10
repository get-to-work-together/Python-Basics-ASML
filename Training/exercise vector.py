
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'<{self._x}, {self._y}>'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def length(self):
        return (self._x ** 2 + self._y **2) ** 0.5

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



# -----------------------

v1 = Vector(1, 6)
print(v1)

v2 = Vector(4, 3)
print(v2)

v3 = v1 + v2
print(v3)

print(v1 > v2)
print(v3 < v2)

vectors = [
    Vector(1, 6),
    Vector(2, 6),
    Vector(1, 3),
    Vector(4, 8),
    Vector(2, 3),
]
print(sorted(vectors))