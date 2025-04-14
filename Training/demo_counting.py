
counter = 0
while counter < 10:
    print(counter := counter + 1)


for counter in [1,2,3,4,5,6,7,8,9,10]:
    print(counter)


for counter in range(10, 0, -1):
    print(counter)


magicnumber = 13

for i in range(1, 21):
    if i == magicnumber:
        break
    print(i)

for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)
