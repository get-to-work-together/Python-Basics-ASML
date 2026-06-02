import math

n = 1000000

total = 0
add_or_subtract = True  # True => add, False => subtract
for denominator in range(1, n, 2):
    term = 1 / denominator
    if add_or_subtract:
        total += term
    else:
        total -= term
    add_or_subtract = not add_or_subtract
pi = total * 4





# total = 0
# for denominator in range(1, n, 4):
#     term1 = 1 / denominator
#     term2 = 1 / (denominator + 2)
#     total = total + term1 - term2
#
# pi = total * 4

print(f'The Leibniz approximation of PI is: {pi}')

print(f'The math library has PI is: {math.pi}')