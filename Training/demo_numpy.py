
import numpy as np
import matplotlib.pyplot as plt

numbers = [3,5,6,7,8]

anumbers = np.array(numbers)

print(type(numbers))
print(numbers)

print(type(anumbers))
print(anumbers)

a = np.arange(0, 10, 0.1)
print(a)

x = np.linspace(0, 10, 101)
print(x)

print(x * 100)

m = np.arange(10, 34).reshape(2, 12)
print(m)
print(m.shape)
print(m.ndim)
print(m.transpose())

print(x)
y = np.sin(x)/(x + 1)

print(y)

plt.plot(x, y, color='orange', linewidth=5)
plt.title('y = np.sin(x)/(x + 1)')
plt.ylabel('y')
plt.grid()
plt.show()