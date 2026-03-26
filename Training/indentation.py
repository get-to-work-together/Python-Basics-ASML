
age = int(input('Enter your age: '))

if age < 0:
    print('Invalid age')

elif age > 120:
    print('Not possible.')

elif age < 18:
    print('Teenager')
    print("What's up?")

elif age > 67:
    print('Elder')
    print('How do you do?')

else:
    print('Adult')
    print('Have a good day')