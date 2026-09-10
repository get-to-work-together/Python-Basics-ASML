import math

user_input = input('Give me the radius of a circle: ')
r = float(user_input)

circumference = 2 * math.pi * r
area = math.pi * r ** 2

print('Radius', r)
print('Circumference', circumference)
print('Area', area)
