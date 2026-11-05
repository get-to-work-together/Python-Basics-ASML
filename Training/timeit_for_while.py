from timeit import timeit
import string
import random


def function1():
    for string in strings:
        s = string[0]


def function2():
    for i in range(len(strings)):
        s = strings[i][0]


strings = []
for i in range(10000):
    s = random.choices(string.ascii_letters, k = random.randint(3, 10))
    strings.append(s)


print( timeit(function1, number=10000) )
print( timeit(function2, number=10000) )
