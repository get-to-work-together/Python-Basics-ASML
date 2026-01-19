import math
import random

n_repititions = 10000000

n_inside_circle = 0
for i in range(n_repititions):
    x = random.random()
    y = random.random()
    d = math.sqrt(x**2 + y**2)
    if d <= 1:
        n_inside_circle += 1

pi = (n_inside_circle / n_repititions) * 4

print(pi)
