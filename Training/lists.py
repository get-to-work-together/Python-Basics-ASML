
shoppinglist = ['bread', 'milk']
print(shoppinglist)

shoppinglist.append('eggs')
shoppinglist.append('oranges')
print(shoppinglist)

shoppinglist.insert(0, 'beer')
print(shoppinglist)

fruit = ['apples', 'bananas']
shoppinglist.extend(fruit)
print(shoppinglist)

removed_item = shoppinglist.pop(1)
print(removed_item)
print(shoppinglist)

del shoppinglist[0]
print(shoppinglist)

while 'bananas' in shoppinglist:
    shoppinglist.remove('bananas')
    print(shoppinglist)
print(shoppinglist)

shoppinglist.reverse()
print(shoppinglist)

shoppinglist.sort(reverse=False)
print(shoppinglist)

shoppinglist.sort(reverse=False)
print(shoppinglist)

shoppinglist.sort(key=len)
print(shoppinglist)

print(len(shoppinglist))
print(min(shoppinglist))
print(max(shoppinglist))
print(min(shoppinglist, key=len))

print(sorted(shoppinglist))
print(shoppinglist)

print(all(shoppinglist))
shoppinglist.append('')
print(all(shoppinglist))
shoppinglist.pop()

print(shoppinglist[0])
print(shoppinglist[1])
print(shoppinglist[-1])

shoppinglist[-1] = 'bananas'
print(shoppinglist)

print(shoppinglist[1:3])
print(shoppinglist[:3])
print(shoppinglist[1:])

shoppinglist[1:3] = [100, 101, 102, 103]
print(shoppinglist)

numbers = [324,4356,5677,678,798,87909,90]
print(numbers)
print(len(numbers))
print(sorted(numbers))
print(sum(numbers))
print(numbers)

copy = numbers.copy()
print(numbers)
print(copy)

copy.append(100)
copy.append(999)
copy.append(-4)
copy.sort()
copy.pop(2)
copy.reverse()

print(copy)
print(numbers)

print(numbers + numbers)
print(5 * numbers)

print(numbers.count(5677))
print(numbers.index(5677))

print(numbers[1:-1:2])