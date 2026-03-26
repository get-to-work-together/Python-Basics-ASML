
s = 'The brown fox jumped over the big lazy dog'

print(s)
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())

print(s.startswith('brown'))
print(s.endswith('fox'))
print(s.lower().find('the'))

print(s.lower().count('the'))

print(s.lower().replace('the', 'XXX'))

s = s.lower().replace('the', 'XXX')

print(s)



