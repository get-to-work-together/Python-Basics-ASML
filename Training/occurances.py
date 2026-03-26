import string

s = """\
Welkom bij Eindhoven.info: De Digitale VVV van de Lichtstad Ontdek Eindhoven, het kloppende hart van de Brainport-regio. Of je nu een inwoner bent van onze groeiende stad met bijna 250.000 inwoners, of een toerist die de innovatieve sfeer van Strijp-S komt proeven: wij wijzen je de weg. Van de beste winkeltips in de binnenstad tot de meest actuele evenementen; Eindhoven.info is jouw onafhankelijke lokale bron voor alles wat er nu gebeurt.
"""

s = s.lower().translate(str.maketrans('', '', string.punctuation))

words = s.split()

unique_words = set(words)

d = {}
for word in unique_words:
    n = words.count(word)
    d[word] = n

for word, n in sorted(d.items()):
    print(f'{word:20}: {n:3} {n * '*'}')
