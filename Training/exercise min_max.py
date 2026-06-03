
def min_max(numbers):
    """Get the minimum and maximum of a list of numbers in one pass"""
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum



# -----------------------------------------------

result = min_max([45, 67, 32, 67, 98, 12])
print(result)

minimum, maximum = min_max([45, 67, 32, 67, 98, 12])
print(f'minimum = {minimum}')
print(f'maximum = {maximum}')