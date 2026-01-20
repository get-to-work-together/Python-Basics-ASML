import random

suits = ['♣️', '♦️', '♥️', '♠️']
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [f'{r}{s}' for s in suits for r in ranks]

print(len(cards))

random.shuffle(cards)

hand = [cards.pop() for _ in range(5)]
print(*hand)

print(len(cards))
