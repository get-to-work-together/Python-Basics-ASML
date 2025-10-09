import string

# s = input('Give some text: ')

s = r"""Eindhoven (uitspraakⓘ) is een stad[1] en gemeente in het zuidoosten van de Nederlandse provincie Noord-Brabant, gelegen in de Brabantse Kempen. Het is naar inwonertal al sinds 1961 de vijfde gemeente van Nederland. Ze telt 248.671 inwoners (30 september 2025) op een grondgebied van 88,92 km². Ze omvat naast de gelijknamige stad Eindhoven tevens het dorp Acht en de uitbreidingslocatie Meerhoven."""

s = s.lower().translate(str.maketrans('', '', string.punctuation))

words = s.split()

unique_words = set(words)

d = {}
for word in unique_words:
    n = words.count(word)
    d[word] = n

for word, n in sorted(d.items(), key=lambda item: item[1]):
    print(f'{word:20}: {n}')










# from collections import Counter
# d = Counter(words)
#
# print(type(d))
# for word, n in d.items():
#     print(f'{word:20}: {n}')
