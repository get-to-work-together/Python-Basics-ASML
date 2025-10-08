def create_banner(s, *, c='*', uppercase=False):
    n = len(s)
    if uppercase:
        s = s.upper()
    line1 = (n + 6) * c
    line2 = c + '  ' + s + '  ' + c
    line3 = (n + 6) * c
    return '\n'.join([line1, line2, line3])


def print_banner(s, **kwargs):
    print(create_banner(s, **kwargs))



# -------------------------------------------------------

# text = input('Give me text: ')
# sign = input('Which character do you want to use? : ')
#
# print_banner(text, c=sign)

print_banner('Abracadabra')
print_banner('Abracadabra', c='#', uppercase=True)


