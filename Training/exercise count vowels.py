
s = input('Give me some text: ').lower()

number_of_a = s.count('a')
number_of_e = s.count('e')
number_of_i = s.count('i')
number_of_o = s.count('o')
number_of_u = s.count('u')

total_number_of_vowels = number_of_a + \
                         number_of_e + \
                         number_of_i + \
                         number_of_o + \
                         number_of_u

total_number_of_vowels = (number_of_a +
                          number_of_e +
                          number_of_i +
                          number_of_o +
                          number_of_u)

print("Number of a's:", number_of_a)
print("Number of e's:", number_of_e)
print("Number of i's:", number_of_i)
print("Number of o's:", number_of_o)
print("Number of u's:", number_of_u)

print("Total number of vowels:", total_number_of_vowels)
