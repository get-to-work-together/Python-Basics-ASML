import numpy as np
import matplotlib.pyplot as plt


x = (np.linspace(0, 10, 101))

print(x)

print(x * 100)

m = np.arange(1, 10).reshape(3, 3)
print(m)
print(m.T)

y = np.sin(x) / (1 + x)
print(y)

plt.plot(x, y, color='orange', lw=3)
plt.grid()
plt.show()

a = np.random.randn(1000)
b = np.random.randn(1000)

plt.scatter(a, b, color='green', alpha=0.5)
plt.grid()
plt.show()


t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]

fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')

fig.colorbar(im, ax=ax, label='Interactive colorbar')

plt.show()