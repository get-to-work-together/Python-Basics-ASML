from copy import deepcopy

shoppinglist = ['bread', 'cheese']
print(shoppinglist)
print(type(shoppinglist))
print(len(shoppinglist))

shoppinglist.append('milk')
shoppinglist.append(42)
print(shoppinglist)

fruit = ['bananas', 'oranges', 'strawberries']
print(fruit)
shoppinglist.extend(fruit)
print(shoppinglist)

print(list('bananas'))

shoppinglist.insert(0, 'beer')
print(shoppinglist)

shoppinglist[4] = 'ham'
print(shoppinglist)

print(shoppinglist[3:5])
shoppinglist[3:5] = ['candy', 'cookies', 'chocolate']
print(shoppinglist)

shoppinglist.reverse()
print(shoppinglist)

shoppinglist.sort(reverse=True)

print('sorted list')
print(shoppinglist)

copy = deepcopy(shoppinglist)
print('Copied', copy)

sorted_shoppinglist = sorted(shoppinglist)
print(sorted(shoppinglist))

del shoppinglist[0]
print(shoppinglist)

del shoppinglist[-3:]
print(shoppinglist)

removed = shoppinglist.pop()
print(removed)
print(shoppinglist)

removed = shoppinglist.pop(0)
print(removed)
print(shoppinglist)

shoppinglist.insert(3, 'candy')
print(shoppinglist)

shoppinglist.remove('candy')
print(shoppinglist)

if 'candy' in shoppinglist:
    shoppinglist.remove('candy')
print(shoppinglist)

for item in sorted(shoppinglist):
    print(item)

for item in reversed(shoppinglist):
    print(item)

name = 'Peter'
print(name[::-1])

print('Copied', copy)

print(min(shoppinglist))
print(max(shoppinglist))

numbers = [34,76,2,7,998,35,66, 7, 35, 7]
print(sorted(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print('abc' + 'def')
print(sorted([2,4,6] + [7,1,9]))

print(numbers)
print(numbers.count(7))
print(numbers.index(7))
print(numbers.index(7, 4))

s = 'The quick brown     fox jumps over the lazy dog'
print(s)
words = s.split()
print(words)

print('-'.join(words))

ranks = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')
print(ranks)

print(numbers)

cubes = [number ** 3 for number in numbers if number > 30]
print(cubes)

cubes = []
for number in numbers:
    if number > 30:
        cubes.append(number ** 3)
print(cubes)

print(words)
print([word[0] + '.' + word[-1]  for word in words if len(word) > 3])