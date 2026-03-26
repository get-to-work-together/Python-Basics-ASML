
age = int(input('Enter your age: '))

if age < 0:
    print('Invalid age')

elif age < 2:
    print('Baby')

elif age >= 2 and age < 4:
    print('Toddler')

elif 4 <= age < 13:
    print('Kid')

elif age < 20:
    print('Teenager')

elif age < 65:
    print('Adult')

elif age < 120:
    print('Elder')

else:
    print('Not humanly possible')
