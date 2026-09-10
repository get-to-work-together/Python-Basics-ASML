import statistics

shoppinglist = ['bread', 'butter', 'milk']
print(shoppinglist)
print(len(shoppinglist))

shoppinglist.append('apples')
shoppinglist.append('bananas')
print(shoppinglist)

shoppinglist.insert(3, 'peanutbutter')
print(shoppinglist)

shoppinglist.pop()
shoppinglist.pop(1)
print(shoppinglist)

shoppinglist.append('milk')
shoppinglist.append('milk')
shoppinglist.append('milk')
print(shoppinglist)
shoppinglist.remove('milk')
print(shoppinglist)

while 'milk' in shoppinglist:
    shoppinglist.remove('milk')

print(shoppinglist[1])
print(shoppinglist[3:])

del shoppinglist[3:]
print(shoppinglist)

drinks = ['beer', 'wine', 'water', 'cola']
shoppinglist.extend(drinks)
print(shoppinglist)

shoppinglist[3], shoppinglist[0] = shoppinglist[0], shoppinglist[3]
print(shoppinglist)
print(sorted(shoppinglist))

shoppinglist.sort()
print(shoppinglist)
print(shoppinglist[::-1])

shoppinglist.reverse()
print(shoppinglist)

print('beer' in shoppinglist)
print(shoppinglist.count('beer'))
print(shoppinglist.index('beer'))

numbers = [23, 45, 67, 798, 12, 4]
print(numbers)
print(sorted(numbers))
print(sorted(numbers, reverse=True))

numbers.sort(reverse=True)
print(numbers)
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(statistics.mean(numbers))

new_list = numbers + numbers
new_list = 10 * numbers
print(new_list)

print(numbers)

cubes = [number ** 3 for number in numbers if number > 10]
print(cubes)

shoppinglist.extend(3 * ['milk'])
print(shoppinglist)

shoppinglist = [item for item in shoppinglist if item != 'milk']
print(shoppinglist)

