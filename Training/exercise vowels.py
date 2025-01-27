s = input('Enter text: ')

number_of_a_characters = len(s)

number_of_a = s.lower().count('a')
number_of_e = s.lower().count('e')
number_of_i = s.lower().count('i')
number_of_o = s.lower().count('o')
number_of_u = s.lower().count('u')

number_of_vowels = number_of_a + number_of_e + number_of_i + number_of_o + number_of_u

print('Text:', s)
print(f'This text has {number_of_a_characters} characters.')
print(f'The "a" was found {number_of_a} times.')
print(f'The "e" was found {number_of_e} times.')
print(f'The "i" was found {number_of_i} times.')
print(f'The "o" was found {number_of_o} times.')
print(f'The "u" was found {number_of_u} times.')
print(f'This text has {number_of_vowels} vowels.')



for vowel in 'aeiou':
    n = s.lower().count(vowel)
    print(f'The "{vowel}" was found {n} times.')
