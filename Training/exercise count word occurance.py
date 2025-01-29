import string
from pprint import pprint


s = """\
Unicode has code points for the 52 cards of the standard French deck plus the Knight (Ace, 2–10, Jack, Knight, Queen, and King for each suit), three for jokers (red, black, and white), and a back of a card, in block Playing Cards (U+1F0A0–1F0FF). Also, a specific fool and twenty-one generic trump cards are added. The depiction of these trump cards in most supporting fonts is based on the Bourgeois Tarot.
Four Knights of the Tarot deck are in block Playing Cards (U+1F0A0–1F0FF). A specific white joker, a fool, and twenty-one generic trump cards were added to the Playing Cards block in Unicode 7.0 with the reference description being not the Italian-suited Tarot de Marseille or its derivatives (which are often used in cartomancy) but the French Tarot Nouveau used to play Jeu de tarot, which is used for divination less frequently."""


s = s.lower().translate(str.maketrans('', '', string.punctuation))

words = s.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    n = words.count(word)
    d[word] = n

for word, n in sorted(d.items()):
    print(f'{word:20}: {n:3} {'*' * n}')

pprint(d)


# or

d = {word: words.count(word) for word in set(words)}

# or

d = dict()
for word in words:
    n = d.get(word, 0) + 1
    d[word] = n

# or

from collections import Counter
d = Counter(words)


