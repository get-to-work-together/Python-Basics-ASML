sentence = 'abracadabra this is a story about a couple of kids walking through the woods'

words = sentence.split()


def number_of_vowels(word):
    return sum(word.count(v) for v in 'aeiou'), word

print( sorted(words, key = number_of_vowels) )

# or

print( sorted(words, key = lambda word: sum(word.count(v) for v in 'aeiou') ))


print(words)
print( list(map(lambda word: sum(word.count(v) for v in 'aeiou'), words)) )

print(words)
print( list(filter(lambda word: sum(word.count(v) for v in 'aeiou') > 1, words)) )
