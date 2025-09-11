
def number_of_o(word):
    return word.count('o')

def number_of_e(word):
    return word.count('e')

lambda word: word.count('e')





words = 'The fox jumped over the big brown dog'.lower().split()

print(sorted(words))

print(sorted(words, key=len))
print(sorted(words, key=len, reverse=True))

print(sorted(words, key=number_of_o))
print(sorted(words, key=lambda word: word.count('o')))
print(sorted(words, key=lambda word: (len(word), word.count('o'))))
