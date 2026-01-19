age = int(input('What is your age? : '))

if age < 0:
    print('Invalid age')
elif age < 2:
    print('Baby')
elif age < 4:
    print('Todler')
elif age < 13:
    print('Kid')
elif age < 20:
    print('Teenager')
elif age < 65:
    print('Adult')
else:
    print('Elder')