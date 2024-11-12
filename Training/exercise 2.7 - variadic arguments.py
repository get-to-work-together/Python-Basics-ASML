import random


def min_max(*numbers):
    lowest = numbers[0]
    highest = numbers[0]
    for number in numbers[1:]:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    return lowest, highest



print( min_max(3, 6, 8, 5, 1, 3, 5) )




numbers = [random.randint(1, 100) for _ in range(20)]

print(numbers)
print( min(numbers), max(numbers) )
print( min_max(*numbers) )



def my_func(*args, **kwargs):
    print(args)
    print(kwargs)

my_func(1, 2, 3, factor=10, offset=100)