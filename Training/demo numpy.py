
import numpy as np

a = np.arange(1, 11)

print(a)
print(type(a))

matrix = a.reshape(2, 5)
print(matrix)

print(np.arange(1, 10).reshape(3, 3))

cubes = a ** 3
print(cubes)

print(a[a % 3 == 0])