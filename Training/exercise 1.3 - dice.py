import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
dice5 = random.randint(1, 6)

total = dice1 + dice2 + dice3 + dice4 + dice5

print('Thrown:', dice1, dice2, dice3, dice4, dice5)
print('Total:', dice1 + dice2 + dice3 + dice4 + dice5)




# dice = []
# for i in range(20):
#     dice.append(random.randint(1, 6))
#
# print('Thrown:', dice)
# print('Total:', sum(dice))
