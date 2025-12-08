gender = 'v'
age = 45

if gender == 'm':
    print('M')

    if age < 21:
        print('boy')
    else:
        print('man')
elif gender == 'v' :
    print('V')
    
    if age < 21:
        print('girl')
    else:
        print('woman')
else:
    print('other')

print('Done')


counter = 1
while counter <= 10:
    print(counter)
    counter += 1



for c in 'abcdefg':
    print(c)

for number in [23,45,78,54]:
    print(number)

for n in range(1, 21):
    print(n)

print()

magic_number = 13

for n in range(1, 21):
    if n == magic_number:
        break
    print(n)

print()

for n in range(1, 21):
    if n == magic_number:
        continue
    print(n)


while True:
    number = int(input('Enter an number between 1 and 10: '))
    if 1 <= number <= 10:
        break
print('The number is %d' % number)
