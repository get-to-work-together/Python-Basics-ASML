from timeit import timeit

def function1():
    for string in strings:
        s = string[0]


def function2():
    for i in range(len(strings)):
        s = strings[i][0]

import os
print(os.getcwd())
with open('10-million-password-list-top-1000000.txt') as f:
    strings = f.readlines()


print( timeit(function1) )
print( timeit(function2) )
