names = []

while True:
    name = input('Enter a name: ')

    if name == '':
        break
    else:
        names.append(name)


print('\nThe entered names are:')

# print(names)

for name in sorted(names):
    print(name)
