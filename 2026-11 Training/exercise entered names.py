names = []
while True:
    name = input('Enter a name: ').strip()
    if name == '':
        break
    names.append(name)

print('\nThe names you entered where:')
for name in sorted(names):
    print(name)
