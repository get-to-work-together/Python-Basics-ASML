
def banner(s, c = '*'):
    n = len(s)
    print((n + 6) * c)
    print(c + '  ' + s + '  ' + c)
    print((n + 6) * c)


def create_banner(s, c = '*'):
    n = len(s)
    banner =  (n + 6) * c + '\n'
    banner +=  c + '  ' + s + '  ' + c + '\n'
    banner += (n + 6) * c
    return banner


def print_banner(s, c = '*'):
    print(create_banner(s, c))


if __name__ == '__main__':

    banner('abracadabra')
    banner('abracadabra', '#')
    banner('abracadabra', '$')

    print(create_banner('Peter', '+'))