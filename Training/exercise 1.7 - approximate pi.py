import math
print(f'π from math = {math.pi}')

n = 10_000_000

total = 0
add_or_subtract = True
for i in range(1, n, 2):
    if add_or_subtract:
        total += 1/i
    else:
        total -= 1/i
    add_or_subtract = not add_or_subtract

pi = total * 4

print(f'π = {pi}')




from fractions import Fraction

total = Fraction(0, 1)
add_or_subtract = True
for i in range(1, n, 2):
    if add_or_subtract:
        total += Fraction(1, i)
    else:
        total -= Fraction(1, i)
    add_or_subtract = not add_or_subtract

pi = float(total * 4)

print(f'π = {pi}')
