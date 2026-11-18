import string
import time

s = """\
ASML is gevestigd in Veldhoven en daar zijn we trots op. Onze campus blijft zich ontwikkelen. Dit is nodig om te kunnen voldoen aan de toenemende vraag naar onze chipmachines. Die zijn nodig omdat mensen steeds meer digitale toepassingen gebruiken, en ook om bijvoorbeeld de duurzame energietransitie mogelijk te maken. 
ASML groeit binnen de grenzen van de campus, maar ook daarbuiten. Over deze ontwikkelingen willen we je graag op de hoogte houden.
ASML ontwikkelt de campus op meerdere locaties. Er vinden uitbreidingen plaats op De Run 6000 en De Run 7000. Op De Run 1000 bereiden we de bouw van een parkeergarage voor. Daarnaast werkt ASML aan een nieuwe campus op Brainport Industries Campus (BIC) Noord in Eindhoven, bedoeld als tweede grote campus voor de lange termijn.
"""

s = s.lower().strip().translate(s.maketrans('', '', string.punctuation))

words = s.split()

t0 = time.thread_time_ns()

# unique_words = set(words)
#
# d = dict()
# for word in unique_words:
#     n = words.count(word)
#     d[word] = n
#
# for word, n in sorted(d.items()):
#     print(f'{word:20}: {n:3} {n * '*'}')

d = {}
for word in words:
    d[word] = d.get(word, 0) + 1

for word, n in sorted(d.items()):
    print(f'{word:20}: {n:3} {n * '*'}')

t1 = time.thread_time_ns()
print(f'\nDuration: {(t1 - t0)//1000}μs')