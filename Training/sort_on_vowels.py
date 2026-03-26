
s = 'this is a piece of beautiful text entered at the end of the day'
words = s.split()

print(words)

def sorts(key):
    jump_table = {
        'vowels': lambda word: sum(word.count(c) for c in 'aeiou'),
        'klm': lambda word: sum(word.count(c) for c in 'klm')
    }
    return jump_table.get(key)

print(sorted(words, key = sorts('klm')))

print(list(map(lambda word: sum(word.count(c) for c in 'aeiou'), words)))

print(list(filter(lambda word: sum(word.count(c) for c in 'aeiou') > 1, words)))

print(list(filter(lambda word: 'i' in word, words)))
