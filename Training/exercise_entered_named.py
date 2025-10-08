# Get the names until no name has been entered
names = []
while True:
    name = input('Give me a name: ').strip()

    if name:
        names.append(name)
    else:
        break

# Print out the sorted names
for name in sorted(names):
    print(name)
