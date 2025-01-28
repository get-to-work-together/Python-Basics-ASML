import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
dice5 = random.randint(1, 6)

print('Thrown:', dice1, dice2, dice3, dice4, dice5)
print('Total:', dice1 + dice2 + dice3 + dice4 + dice5)

# or using a for loop and a list

dice = []
for _ in range(5):
    dice.append(random.randint(1, 6))

print('Thrown:', dice)
print('Total:', sum(dice))
