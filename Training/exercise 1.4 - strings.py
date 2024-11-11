s = input('Enter text: ')

print('Original text', s)

print('Uppercase:', s.upper())
print('Lowercase:', s.lower())
print('Capitalize:', s.capitalize())
print('Title:', s.title())

print('Ends with a ?:', s.endswith('?'))
print('Ends with a ?:', s[-1]=='?')

print('Snake case:', s.lower().replace(' ', '_'))
