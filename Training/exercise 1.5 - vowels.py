s = input('Enter some text: ')

number_of_a = s.lower().count("a")
number_of_e = s.lower().count("e")
number_of_i = s.lower().count("i")
number_of_o = s.lower().count("o")
number_of_u = s.lower().count("u")

number_of_vowels = number_of_a + number_of_e + number_of_i + number_of_o + number_of_u

print(f'Found the vowel "a" {number_of_a} times')
print(f'Found the vowel "e" {number_of_e} times')
print(f'Found the vowel "i" {number_of_i} times')
print(f'Found the vowel "o" {number_of_o} times')
print(f'Found the vowel "u" {number_of_u} times')

print(f'Total number of vowels is {number_of_vowels}')

print(f'Total length of the text is {len(s.replace(" ", ""))}')


counts = []
for vowel in 'aeiou':
    n = s.lower().count(vowel)
    counts.append(n)
    print(f'Found the vowel {vowel} {n} times')
print(counts)
print(f'Total number of vowels is {sum(counts)}')

