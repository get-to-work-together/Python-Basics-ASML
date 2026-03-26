import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
dice5 = random.randint(1, 6)

total = dice1 + dice2 + dice3 + dice4 + dice5

print(dice1, dice2, dice3, dice4, dice5)
print('total:', total)

total = 0
for _ in range(10):
    dice = random.randint(1, 6)
    total += dice
    print(dice)
print('total', total)

total = 0
dice = []
for _ in range(10):
    dice.append(random.randint(1, 6))

print(dice)
print(dice[3])
print('total', total)

print(80 * '-')

magicnumber = 11

for i in range(1, 21):
    if i == magicnumber:
        break
    print(i)

print(80 * '-')

for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)