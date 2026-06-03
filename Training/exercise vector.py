
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'[{self._x}, {self._y}]'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def __lt__(self, other):
        return self.length() < other.length()
    def __le__(self, other):
        return self.length() <= other.length()
    def __gt__(self, other):
        return self.length() > other.length()
    def __ge__(self, other):
        return self.length() >= other.length()

# ---------------------------

a = Vector(1, 5)
b = Vector(4, 2)

print(a)
print(b)

c = a + b
print(c)

print( 123 + 678 )
print( 'abc' + 'def' )
print( [1,3,5] + [9, 7])

print( 234 < 736)
print( 'abc' < 'xyz' )

print(a > b)