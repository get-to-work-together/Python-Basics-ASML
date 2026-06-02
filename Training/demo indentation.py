gender = 'm'

if gender == 'm':
    print('Dear Sir')

elif gender == 'v':
    print('Dear madam')

else:
    print('Dear person')

print('How do you do?')


for number in [3, 7, 6, 5]:
    print(number)

for c in 'abcdefg':
    print(c)

for number in range(1, 11):
    print(number)


magicnumber = 13

for i in range(1, 21):
    if i == magicnumber:
        break
    print(i)

for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)
