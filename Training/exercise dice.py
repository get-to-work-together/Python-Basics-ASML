import random

# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)
# dice3 = random.randint(1, 6)
# dice4 = random.randint(1, 6)
# dice5 = random.randint(1, 6)
#
# total = dice1 + dice2 + dice3 + dice4 + dice5

dice = []
for i in range(10):
    die = random.randint(1, 6)
    dice.append(die)

total = sum(dice)

print('Thrown:', dice)
print('Total:', total)
