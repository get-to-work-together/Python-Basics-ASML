from demo_looping import magicnumber

counter = 1
while counter <= 10:
    print(counter)
    counter += 1


for number in [1,2,4,7,8,9,10]:
    print(number)


for number in range(10, 0, -1):
    print(number)


names = ['Peter', 'Bob', 'Grace']

for name in names:
    print(name)

for i in range(len(names)):
    print(names[i])



magicnumber = 13

for i in range(1, 21):
    if i == magicnumber:
        print('Found it')
        break
    print(i)

for i in range(1, 21):
    if i == magicnumber:
        print('Found it')
        continue
    print(i)