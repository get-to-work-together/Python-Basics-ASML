
s = input('Give me some text: ')

print('Original:', s)

print('Upper:', s.upper())
print('Lower:', s.lower())
print('Capitalize:', s.capitalize())
print('Title:', s.title())

print('Ends with a ?:', s.endswith('?'))
print('Ends with a ?:', s[-1] == '?')

print('Contains a ?:', s.__contains__('?'))
print('Contains a ?:', '?' in s)

print('snake_case:', s.lower().replace(' ', '_'))
print('PascalCase:', s.title().replace(' ', ''))
print('camelCase:', s[0].lower() + s.title().replace(' ', '')[1:])

