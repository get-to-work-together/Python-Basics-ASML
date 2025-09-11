magicnumber = 11

for i in range(1, 21):
    print(i)

print(80*'-')

for i in range(1, 21):
    if i == magicnumber:
        break
    print(i)

print(80*'-')

for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)