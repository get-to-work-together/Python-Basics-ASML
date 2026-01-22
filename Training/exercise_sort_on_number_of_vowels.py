s = 'oledie bananas The big brown fox jumped over the lazy dog abracadabra'
# s = input('Enter some text: ')

words = s.lower().split()

words.sort(key = lambda w: sum(w.count(v) for v in 'aeiou'))

for word in words:
    print(word)