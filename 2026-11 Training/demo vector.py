
class Vector:

    def __init__(self, x: int|float, y: int|float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return "Submarine"

    def __eq__(self, other):
        return self.length == other.length
    def __ne__(self, other):
        return self.length != other.length
    def __gt__(self, other):
        return self.length > other.length
    def __ge__(self, other):
        return self.length >= other.length
    def __lt__(self, other):
        return self.length < other.length
    def __le__(self, other):
        return self.length <= other.length

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# -------------------------------


v1 = Vector(4, 3.2)
v2 = Vector(2, 3)

print(v1)
print(v2)

v3 = v1 + v2

print(v3)

print(v1.length)
print(v2.length)
print(v3.length)

if v1 >= v2:
    print('v1 is longer than v2')
else:
    print('v1 is shorter than v2')

print(v1 - v2)