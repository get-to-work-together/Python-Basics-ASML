counter = 0
while counter < 10:
    print(counter)
    counter += 1

print()

for i in [2, 4, 6, 7, 8]:
    print(i)

for c in 'abcdefg':
    print(c)

for s in ['this', 'is', 'awesome']:
    print(s)

for number in range(1, 11):
    print(number)

for number in range(1, 11, 2):
    print(number)

print()
magic_number = 13
for number in range(1, 21):
    if number == magic_number:
        break
    print(number)

print()
for number in range(1, 21):
    if number == magic_number:
        continue
    print(number)
