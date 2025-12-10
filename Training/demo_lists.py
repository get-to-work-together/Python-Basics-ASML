

numbers = [1,2,3,4,5]

numbers.append(6)
numbers.extend([7, 8, 9])

numbers.insert(len(numbers), [2,3,4])

print(numbers)



numbers = [1,2,3,4,5]

print(numbers + [7, 8, 9])

print(numbers)



numbers = [1,2,3,4,5]

print(numbers[2:3])

numbers[2:2] = [99, 99, 99]

print(numbers)


numbers = [4,8,5,7,2]

for n in sorted(numbers):
    print(n)


s = 'abcdefg'

print('x' in s)