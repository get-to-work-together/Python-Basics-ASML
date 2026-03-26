import random

suits = list('♣♦♥♠')
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

print(suits)
print(ranks)

cards = [f'{r}{s}' for s in suits for r in ranks]
print(cards)
print(len(cards))

random.shuffle(cards)

hand = [cards.pop() for _ in range(5)]
print(hand)