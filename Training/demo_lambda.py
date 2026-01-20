
def calculate_sum(a, b):
    return a + b

f = lambda a, b: a + b

print(calculate_sum(1,2))
print(f(1,2))

words = 'The big brown fox jumps over the lazy dog'.lower().split()


for word in sorted(words, key = lambda s: s.count('a')):
    print(word)