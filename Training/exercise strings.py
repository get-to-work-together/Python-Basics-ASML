s = input('Enter a string: ')

print('Original:', s)
print('Lower:', s.lower())
print('Upper:', s.upper())
print('Capitalize:', s.capitalize())
print('Title:', s.title())
print('Ends with ?:', s.endswith('?'))
print('Snake case:', s.lower().replace(' ', '_'))
