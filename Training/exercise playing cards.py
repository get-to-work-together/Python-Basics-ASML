import random

suits = ['\u2663', '\u2666', '\u2665', '\u2660']
suits = ['♣', '♦', '♥', '♠']
suits = ['\u2663\uFE0E', '\u2666\uFE0F', '\u2665\uFE0F', '\u2660\uFE0E']
suits = '♣️ ♦️ ♥️ ♠️'.split()

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

print(suits)
print(ranks)

deck = [suit + rank for suit in suits for rank in ranks]

print(deck)
print(len(deck))

random.shuffle(deck)

print(deck)

hand = sorted([deck.pop() for _ in range(5)])

print(hand)
print(len(deck))

print(f'Your hand is: {' '.join(hand)}')

