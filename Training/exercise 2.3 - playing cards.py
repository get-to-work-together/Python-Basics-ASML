import random

suits = '♣ ♢ ♡ ♠'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

deck = [f'{r}{s}' for s in suits for r in ranks]

random.shuffle(deck)

hand = [deck.pop() for _ in range(5)]

print(hand)
