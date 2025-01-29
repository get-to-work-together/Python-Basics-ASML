
numbers = [12, 34, 56, 78, 76, 43, 27]

hundreds = [number * 100 for number in numbers]

print(hundreds)


hundreds = []
for number in numbers:
    hundreds.append(number * 100)

print(hundreds)


hundreds = [number * 100 for number in numbers if number % 2 == 0]

print(hundreds)



hundreds = []
for number in numbers:
    if number % 2 == 0:
        hundreds.append(number * 100)

print(hundreds)


words = 'the brown fox jumped over the lazy dog'.split()
print(words)

first_and_last = [word[0] + word[-1] for word in words]
print(first_and_last)


print([x ** 2 for x in range(1, 11)])