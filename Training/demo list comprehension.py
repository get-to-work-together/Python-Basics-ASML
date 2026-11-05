
numbers = [12,234,45,657,867,56,23,2.5]

cubes1 = []
for number in numbers:
    if number > 100:
        cubes1.append(number ** 3)

# or with list comprehension

cubes2 = [number ** 3 for number in numbers if number > 100]

print(cubes1)
print(cubes2)