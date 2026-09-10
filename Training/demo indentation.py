# age = 14
# gender = 'x'
#
#
# if gender == 'm':
#     if age > 21:
#         print('Sir')
#     else:
#         print('Hi dude')
#
# elif gender == 'f':
#     if age > 21:
#         print('Madam')
#     else:
#         print('Bro')
#
# else:
#     print('Love')
#
# print('How do you do?')


# # JAVA: for (int i = 1; i <= 10; i++){}
# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1
#
# # JAVA for (int number: numbers){}
# for number in [2,4,6,5,8,9]:
#     print(number)
#
# import string
# for c in string.ascii_lowercase:
#     print(c)
#
# for number in range(1, 11):
#     print(number)


# magic_number = 13
#
# for n in range(1, 21):
#     print(n)
#
# print(80 * '-')
#
# for n in range(1, 21):
#     if n == magic_number:
#         break
#     print(n)
#
# print(80 * '-')
#
# for n in range(1, 21):
#     if n == magic_number:
#         continue
#     print(n)


for i, c in enumerate('ABGSJDG'):
    print(f'{i}: {c}')