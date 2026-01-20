names = []

while True:
    name = input('Enter a name: ')

    if name == '':
        for name in sorted(names):
            print(name)
        break

    names.append(name)
