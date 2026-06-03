
words = 'the quick fox jumped over the lazy brown dog abracadabra banana'.split()

sorted_words = sorted(words, key = lambda word: sum(word.count(v) for v in 'aeiou'))
print(sorted_words)

sorted_words = sorted(words, key = lambda word: word[::-1])
print(sorted_words)
