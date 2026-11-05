import numpy as np
import matplotlib.pyplot as plt

print(np.__version__)

a = np.arange(1, 11, 0.1)
print(type(a))

a = np.linspace(1, 10, 91)
print(a)

# vectorized!!!
print(a * 100)

m = np.arange(1, 13).reshape(3, 4)
print(m)
print(m.transpose())

x = np.linspace(0, 10, 100)
y = np.sin(x)/(x + 1)

plt.plot(x, y, color='purple', linewidth=3)
plt.grid()
plt.show()