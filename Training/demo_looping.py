
# s = 'abcdefg123'
#
# for c in s:
#     print(c)

# n0 = 12
# n1 = 23
#
# magic_number = 13
# for n in range(n0, n1+1):
#     if n == magic_number:
#         continue
#     print(n)


while True:
    number = int(input('Enter an number between 1 and 10: '))
    if 1 <= number <= 10:
        break

print('The number is %d' % number)
