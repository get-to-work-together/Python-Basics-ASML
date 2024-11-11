age = int(input('How old are you? '))

if age < 2:
    print('Baby. Bah Bah')

elif 2 <= age < 4:
    print('Toddler. Mama')

elif 4 <= age < 13:
    print('Kid. Playing')

elif 13 <= age < 20:
    print('Teenager. Gaming')

elif 20 <= age < 65:
    print('Adult. Work')

else:
    print('Elder. Please show some respect')