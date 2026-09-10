
age = int(input('Enter age: '))

if 0 <= age < 2:
    print('Baby')

elif 2 <= age < 4:
    print('Toddler')

elif 4 <= age < 13:
    print('Kid')

elif 13 <= age < 20:
    print('Teenager')

elif 20 <= age < 65:
    print('Adult')

elif 65 <= age < 120:
    print('Elder')

else:
    print('Invalid age')
