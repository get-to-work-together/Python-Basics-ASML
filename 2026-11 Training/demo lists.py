
shopping_list = ['milk', 'bread', 'oranges']

shopping_list.append('cheese')
shopping_list.append('bananas')
shopping_list.insert(0, 'beer')
del shopping_list[2]
shopping_list.pop()
shopping_list.extend(['toothpaste', 'shampoo', 'soap'])
shopping_list.append('beer')
shopping_list.append('beer')

# shopping_list.append(12345)

while 'beer' in shopping_list:
    shopping_list.remove('beer')

shopping_list.sort()
shopping_list.reverse()

print(shopping_list)

for item in shopping_list:
    print(item)


s = 'abcdefg'
print(list(s))

sorted_list = sorted(shopping_list)
print(shopping_list)
print(sorted_list)