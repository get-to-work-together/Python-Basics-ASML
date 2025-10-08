s = input('Give some text: ').lower()

number_of_a = s.count('a')
number_of_e = s.count('e')
number_of_i = s.count('i')
number_of_o = s.count('o')
number_of_u = s.count('u')

number_of_vowels = (number_of_a +
                    number_of_e +
                    number_of_i +
                    number_of_o +
                    number_of_u)

print(f"Found the vowel 'a' {number_of_a} times")
print(f"Found the vowel 'e' {number_of_e} times")
print(f"Found the vowel 'i' {number_of_i} times")
print(f"Found the vowel 'o' {number_of_o} times")
print(f"Found the vowel 'u' {number_of_u} times")

print(f"Total number of characters: {len(s)}")

print(f"Total number of non-whitespace characters: {len(s.replace(' ', ''))}")

print(f"Total number of vowels: {number_of_vowels}")











# number_of_vowels = 0
#
# for vowel in 'aeiou':
#   n = s.count(vowel)
#   number_of_vowels += n
#
#   print(f'The vowel {vowel} occurs {n} times.')
#
# print(f"Total number of characters: {len(s)}")
# print(f"Total number of vowels: {number_of_vowels}")
