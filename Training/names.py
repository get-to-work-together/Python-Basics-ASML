names = []

while True:
    name = input(f'Enter a name: ')
    if name != '':
        names.append(name)
    else:
        break

print('The names you entered are:')
for name in sorted(names, key=str.lower):
    print(name)