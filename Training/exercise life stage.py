age = int(input('How old are you? '))

if age < 0:
    print('Invalid age!')

elif age < 2:
    print('Baby')

elif age < 4:
    print('Toddler')

elif age < 13:
    print('Kid')

elif age < 20:
    print('Teenager')

elif age < 65:
    print('Adult')

elif age < 120:
    print('Elder')

else:
    print('That cannot be true!!!!')

