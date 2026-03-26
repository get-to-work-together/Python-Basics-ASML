s = input('Enter a string: ')

print('Original string:', s)

print('Uppercase:', s.upper())
print('Lowercase:', s.lower())
print('Capitalize:', s.capitalize())
print('Title:', s.title())

print('Ends with ?:', s.endswith('?'))
print('Ends with ?:', s[-1] == '?')

print('snake_case:', s.lower().replace(' ', '_'))
