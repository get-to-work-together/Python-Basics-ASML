import numpy as np
import matplotlib.pyplot as plt


a = np.array( [1,2,3,4,5,6,7,8] )
print(type(a))
print(a)

print(a * 100)

print(a.reshape(2, 4))

x = np.arange(1, 11, 0.1)
x = np.linspace(1, 10, 101)
print(x)

y = np.sin(x) / x
print(y)

plt.plot(x, y, color='darkred', linewidth=3)
plt.grid()
plt.show()