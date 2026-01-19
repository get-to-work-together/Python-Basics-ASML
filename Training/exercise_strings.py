s = input('Enter a string: ')

print(s)

print('lower:', s.lower())
print('upper:', s.upper())
print('capitalize:', s.capitalize())
print('title:', s.title())
print('swapcase:', s.swapcase())

print('endswith ?:', s.endswith('?'))

print('snake_case:', s.lower().replace(' ', '_'))
