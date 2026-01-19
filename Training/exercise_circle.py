import math

user_input  = input('Enter the radius of a circle: ')
radius = float(user_input)

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('The radius of the circle is: %f' % radius)
print('The area of the circle is: %f' % area)
print('The circumference of the circle is: %f' % circumference)
