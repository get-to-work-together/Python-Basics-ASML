import string

s = """\
Eindhoven (uitspraakⓘ) is een stad[1] en gemeente in het zuidoosten van de Nederlandse provincie Noord-Brabant, gelegen in de Brabantse Kempen. Het is naar inwonertal al sinds 1961 de vijfde gemeente van Nederland. Ze telt 249.873 inwoners (1 januari 2026) op een grondgebied van 88,92 km². Ze omvat naast de gelijknamige stad Eindhoven tevens het dorp Acht en de uitbreidingslocatie Meerhoven.
De gemeente maakt deel uit van de Metropoolregio Eindhoven (MRE) en het stedelijk netwerk BrabantStad. Het stadsgewest Eindhoven (niet te verwarren met de metropoolregio), bestaande uit onder andere de gemeenten Eindhoven, Veldhoven, Best, Nuenen c.a. en Geldrop-Mierlo, telt bijna 420.000 inwoners op een oppervlakte van ongeveer 540 km². In de MRE wonen ongeveer 810.000 mensen.
Het tweede woorddeel kan slaan op Hof (omheind stuk grond, tuin, aarde) of op Hoeve (hofstede). De oorsprong van beide woorden is verschillend, maar later zijn deze in hun gebruik ongeveer samengevallen en kregen ze de betekenis die we nu kennen: een gebouw met omliggende gronden ten behoeve van de exploitatie. De herkomst van het eerste woorddeel is veel minder duidelijk. Vermoedelijk werd met Eind de grens bedoeld tussen de cultuurgrond van een nederzetting en de woeste grond daarbuiten. De plaatsnaam kan dus geïnterpreteerd worden als 'het hof of de hoeve aan de grens tussen cultuurgrond en woeste grond'.[2]"""

s = s.lower().translate(s.maketrans('', '', string.punctuation))

words = s.split()

unique_words = [word for word in set(words) if not word.isdecimal()]

d = {}
for word in unique_words:
    n = words.count(word)
    d[word] = n

for word, n in sorted(d.items()):
    print(f'{word:20}: {n:3} {n * '*'}')
