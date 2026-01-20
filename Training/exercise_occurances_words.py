import string

text = """The Playing Cards block contains one emoji: U+1F0CF 🃏 PLAYING CARD BLACK JOKER.[2][3] It defaults to an emoji presentation and has two standardized variants defined to specify emoji-style (U+FE0F VS16) or text presentation (U+FE0E VS15).[4]

The emoji presentation sequences refine and colorize the text presentation of the playing card suits. ♠︎♥︎♦︎♣︎ becomes ♠️♥️♦️♣️. This was done by appending the U+FE0F code point to the textual code points shown far above. For example, the black heart suit &#x2665; becomes the red heart emoji by &#x2665;&#xFE0F;. Conversely, the black heart suit can be coerced by appending U+FE0E with &#x2665;&#xFE0E;. These hold for each suit.[5]

There is an emoji for Japanese hanafuda (flower playing cards): U+1F3B4 🎴 FLOWER PLAYING CARDS. The emoji can stand for any hanafuda card but it is usually depicted as the Moon card specifically."""

# Remove unicode characters
# IMPORTANT: Also remove diacritical characters like ë. Hmmm probably not what you want
clean_text = text.encode("ascii", "ignore").decode("ascii")

# Remove punctuation
s = clean_text.lower().translate(str.maketrans('', '', string.punctuation))

# Get all words
words = s.split()

# Get unique words
unique_words = set(words)

# Build dictionary with number of occurances per word
d = {}
for word in unique_words:
    d[word] = words.count(word)

# # or
d = {word: words.count(word) for word in set(words)}

# # or
# from collections import Counter
# d = Counter(words)

# output
for word, n in d.items():
    print(f'{word:20}: {n:3}', '*' * n)
