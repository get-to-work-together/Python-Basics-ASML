
n = 1000000
print('Number of increments:', n)

total = 0
for i in range(1, n, 4):
    term_to_add = 1 / i
    term_to_subtract = 1 / (i + 2)
    total = total + term_to_add - term_to_subtract

pi = total * 4

print('The leibniz approximation of PI is:', pi)

import math
print('The value of PI in the math library is:', math.pi)