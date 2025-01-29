names = []
while True:
    name = input('Give a name: ')
    if name:
        names.append(name)
    else:
        break

print('\nThe names you entered were:')
for name in sorted(names):
    print(name)
