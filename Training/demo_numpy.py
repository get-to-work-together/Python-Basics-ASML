import numpy as np

x = np.linspace(0, 10, 11)

y = x * 10

print(x)
print(y)

m = np.arange(1, 19).reshape(3, 6).transpose()
print(m)

x = np.linspace(0, 10, 100)
y = np.sin(x)/(x + 1)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title('y = sin(x)/(x + 1)')
ax.plot(x, y, color='red', lw=5)
ax.grid()
plt.show()
