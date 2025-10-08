import random
from timeit import timeit


def function1():
    c = number in l

def function2():
    c = number in t

def function3():
    c = number in s

def function4():
    s2 = set(l)
    c = number in s2


if __name__ == '__main__':

    low = 0
    high = 999999
    n = 200

    r = random.sample(range(low, high + 1), n)
    l = list(r)
    t = tuple(r)
    s = set(r)

    number = random.randint(low, high)

    print( 'list', timeit(function1, number=1000) )
    print( 'tuple', timeit(function2, number=1000) )
    print( 'set', timeit(function3, number=1000) )
    print( 'list & set', timeit(function4, number=1000) )
