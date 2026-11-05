import math

user_input = input('What is the radius of your circle? : ')

r = float(user_input)

circumference = 2 * math.pi * r
area = math.pi * r ** 2

print('Radius:', r)
print('Circumference:', circumference)
print('Area:', area)

print(f'Radius        : {r:>8.3f}')
print(f'Circumference : {circumference:>8.3f}')
print(f'Area          : {area:>8.3f}')
