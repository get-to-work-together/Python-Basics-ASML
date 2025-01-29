
def print_banner(s, c = '*'):
    n = len(s)
    print((n + 6) * c)
    print(c + '  ' + s + '  ' + c)
    print((n + 6) * c)


# --------------------------------------------------------

name = input('What is your name?: ')
print_banner(name)

print_banner('Peter', '$')
print_banner('Peter', c = '$')
