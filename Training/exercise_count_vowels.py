s = input('Enter a string: ')

number_of_a = s.lower().count('a')
number_of_e = s.lower().count('e')
number_of_i = s.lower().count('i')
number_of_o = s.lower().count('o')
number_of_u = s.lower().count('u')

number_of_vowels = number_of_a + \
                   number_of_e + \
                   number_of_i + \
                   number_of_o + \
                   number_of_u

number_of_vowels = (number_of_a +
                    number_of_e +
                    number_of_i +
                    number_of_o +
                    number_of_u)
print(s)
print()
print(f'The vowel "a" occurs {number_of_a} times')
print(f'The vowel "e" occurs {number_of_e} times')
print(f'The vowel "i" occurs {number_of_i} times')
print(f'The vowel "o" occurs {number_of_o} times')
print(f'The vowel "u" occurs {number_of_u} times')
print()
print(f'The total number of vowels is {number_of_vowels}')