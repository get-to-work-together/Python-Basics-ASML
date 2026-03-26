from math import pi

user_input = input('Enter the radius of a circle: ')
r = float(user_input)

area = pi * r ** 2
circumference = 2 * pi * r

print('Radius of the circle:', r)
print('Area of the circle:', area)
print('Circumference of the circle:', circumference)

