import string

s = '''\
Het GLOW Festival is een gratis lichtkunstfestival in de Nederlandse stad Eindhoven waarop kunstenaars en ontwerpers uit binnen- en buitenland lichtkunst- en designtoepassingen tonen die tot stand zijn gekomen door het gebruik van nieuwe mediatechnologieën, zoals computers, sensoren, animaties, maar ook bekendere projectietechnieken.

Het festival is een openlucht-tentoonstelling waarbij kenmerkende gebouwen en locaties met kunstlicht worden belicht. Tijdens het eerste festival waren in de stad en op de oevers van de Dommel kunstwerken te zien. Doordat het festival steeds groter is geworden, werden Strijp-S en het terrein van TU/e hier bij getrokken.

Door de productie van lucifers en later de gloeilamp door Philips in Eindhoven heeft de stad altijd al iets met licht gehad. Eindhoven staat daarom ook wel bekend als lichtstad. Tegenwoordig is het de led-verlichting die in toenemende mate de aandacht trekt.

Vanwege het COVID-19 virus kon in 2020 het festival niet plaatsvinden.[1]

De editie van 2021 getiteld Moved by Light, vond – in tegenstelling tot andere edities – plaats op vier verschillende locaties in Eindhoven, namelijk Centrum, Strijp S/Strijp T, Campina en TU/e (Technische Universiteit Eindhoven). Daarnaast waren er bij die editie op twee locaties in Eindhoven satelliet-projecten:

Nuenen - De bekende zonnebloemen van Hugo Vrijdag die worden geplaatst bij de molen in Nuenen.

High Tech Campus Eindhoven - Een water- en lichtshow ontworpen door het Franse gezelschap Aquatique Show.'''

s = s.translate(str.maketrans('-', ' ', '.,!?()')).lower()

words = s.split()

unique_words = set(words)

occurances = {}
for word in unique_words:
    n = words.count(word)
    occurances[word] = n

# or
# occurances = {word: words.count(word) for word in set(words)}

for word, n in sorted(occurances.items()):
    print(f'{word:30}: {n:4} {n * "*"}')