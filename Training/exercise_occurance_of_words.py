import string
import time

s = """\
Eindhoven is a municipality and a city located in the province of Noord-Brabant in the south of the Netherlands. The city counts 213,809 inhabitants (1 January 2010), which makes it the fifth-largest city of the Netherlands and the biggest of North-Brabant.
Eindhoven is the 2011 Intelligent Community of the Year.""" * 100

s = s.lower().translate(str.maketrans('áäâà', 'aaaa', string.punctuation + string.digits))

words = s.split()

t0 = time.process_time_ns()
unique_words = set(words)

d = {}
for word in sorted(unique_words):
    d[word] = words.count(word)

# d = {word: words.count(word) or word in sorted(unique_words)}

t1 = time.process_time_ns()
print(f'Option 1 took {t1 - t0}ns.')


t0 = time.process_time_ns()
d = {}
for word in words:
    d[word] = d.get(word, 0) + 1
t1 = time.process_time_ns()
print(f'Option 2 took {t1 - t0}ns.')


t0 = time.process_time_ns()
from collections import Counter
d = dict(Counter(words))
t1 = time.process_time_ns()
print(f'Option 3 took {t1 - t0}ns.')


for word, n in d.items():
    print(f'{word:20}: {n:3}')