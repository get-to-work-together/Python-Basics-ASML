s = input('Enter text: ')

print('The original text:', s)

print('upper:', s.upper())
print('lower:', s.lower())
print('capitalize:', s.capitalize())
print('title:', s.title())

print('Ends with ?:', s.endswith('?'))
print('Ends with ?:', s[-1] == '?')

print('snake_case:', s.lower().replace(' ', '_'))
