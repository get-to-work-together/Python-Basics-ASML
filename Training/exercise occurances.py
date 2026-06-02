import string

s = """\
De door Cees Geenen en Leo Oskam ontworpen Stadsschouwburg werd op 2 oktober 1964 geopend in aanwezigheid van prinses Beatrix. De stadsschouwburg was toen erg modern en vrij uniek in Europa. De eerste directeur was Ben Ullings. Ullings trok veel vernieuwend theater aan, en dit zorgde zelfs voor veel toeloop van toneelliefhebbers uit België. Ullings is opgevolgd door Jan Reijs. Na Reijs werd een directeur benoemd die een arbeidsconflict kreeg met de gemeente Eindhoven. In 1992 werd Fons Bruins benoemd tot directeur.
Eind jaren 90 werd de wens een nieuwe zaal te bouwen steeds groter. Uiteindelijk is de multifunctionele Philipszaal er gekomen en zijn de voormalige Grote Zaal en Globetheater gerenoveerd. De architect voor zowel de renovatie en de nieuwbouw was het Eindhovens Bureau Architecten. Op 16 januari 2007 werd het Parktheater geopend[1]. De nieuwbouw was een initiatief van Fons Bruins die na 14 jaar directeurschap op 3 september 2007 met pensioen ging. Bruins was goed in staat om sponsoren voor het project over de brug te krijgen. Op 3 september 2007 werd hij opgevolgd door de huidige directeur, Giel Pastoor, voormalig directeur van schouwburg De Tamboer in Hoogeveen.
De gemeente Eindhoven heeft het Parktheater in maart 2016 aangewezen als gemeentelijk monument teneinde ze te beschermen tegen afbraak."""

# remove all punctuation characters
s = s.lower().translate(str.maketrans('', '', string.punctuation))

words = s.split()

unique_words = set(words)

d = {} # empty dict
for word in unique_words:
    if not word.isnumeric():
        n = words.count(word)
        d[word] = n

print(d)

for word, n in sorted(d.items()):
    print(f'{word:30}: {n}')

