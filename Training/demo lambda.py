

words = 'the quick fox jumped over the lazy brown dog abracadabra banana'.split()

print(words)

print(sorted(words))

print(sorted(words, reverse=True))

print(sorted(words, key=len))

def number_of_a(word):
    return word.count('a')

number_of_a = lambda word: word.count('a')


print(sorted(words, key=number_of_a, reverse=True))
print(sorted(words, key=lambda word: word.count('a'), reverse=True))
print(sorted(words, key=lambda word: word.count('o'), reverse=True))

print(list(map(len, words)))

def long_words(word):
    return len(word) > 5

lambda word: len(word) > 5


print(list(filter(long_words, words)))
