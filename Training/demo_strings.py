

name = 'Peter'
age = 65


# Peter is 65 years old


print(name, 'is', age, 'years old')
print(name + ' is ' + str(age) + ' years old')
print(f'{name} is {age} years old')
print('{} is {} years old'.format(name, age))
print('%s is %d years old' % (name, age))

s = 'abracadabra'
number_of_a = s.count('a')
print(number_of_a)
print(len(s))


print('first character', s[0])
print('fifth character', s[4])
print('last character', s[-1])
print('second last character', s[-2])

print(s[1:5])
print(s[:3])
print(s[-3:])

position = s.index('cada')
print(position)

print(s[position:position+4])

print('\u2206')
print('∆')