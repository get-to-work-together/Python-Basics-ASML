
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Vector({self._x}, {self._y})'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5


# -------------------------

v1 = Vector(4, 3)
v2 = Vector(3, -2)

print(v1)
print(v2)

v3 = v1 + v2

print(v3)

print(v1.length())
print(v2.length())

print(4 + 5)
print('abc' + 'def')
print([1,2,3] + [4,5,6])


v4 = Vector(3, 4)
l = v4.length()
print(l)

assert l == 5, 'The length is incorrect'