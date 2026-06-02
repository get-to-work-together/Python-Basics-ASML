names = []

while True:
    name = input('Enter a name: ')

    if name:
        names.append(name)
    else:
        break


names = sorted(names)
names.sort()

print(f'You entered {len(names)} names.')
print('The names you entered are:')
for name in names:
    print(name)