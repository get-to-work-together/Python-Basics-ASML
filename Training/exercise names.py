
names = []

while True:
    name = input('Give me a name: ')

    if name == '':
        break

    names.append(name)

print(f'\nYou entered {len(names)} names.')
for name in sorted(names):
    print(name)