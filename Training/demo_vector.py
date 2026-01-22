
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def length(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

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


# ===================================================

v1 = Vector(1, 2)
v2 = Vector(2, 3)

print(v1)
print(v2)

v3 = v1 + v2 + v1
print(v3)

print(v1 > v2)
print(v1 == v2)
print(v1 < v2)
