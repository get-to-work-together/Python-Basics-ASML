import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)
y = np.sin(x) / (x + 1)

y = x ** 2

print(y)

# plt.plot(x, y, color='red', linewidth=3)
# plt.grid()
# plt.show()

m = np.arange(1, 13).reshape(3, 4)
print(m)
print(m.transpose())

x1 = np.array([1,2,3,4,5])
x2 = np.array([1,2,3])
print( np.linalg.outer(x1, x2) )

d = np.arange(1, 101).reshape(2, 5, 5, 2)
print(d.ndim)
print(d[1, 2, 1, 0])

x = np.arange(1, 21)
print(x)

x_slice = x[3:7].copy()
print(x_slice)

x_slice[-1] = 99
print(x_slice)

print(x)

data = np.random.randint(1, 100, 20)
data = np.random.normal(10, 2, 1000)

plt.hist(data, bins=30, color='seagreen')
plt.grid()
plt.legend(['data'])
plt.title('Histogram')
plt.show()