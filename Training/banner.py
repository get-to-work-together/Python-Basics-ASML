
def print_banner(s: str, c: str = '*'):
    """Print a banner with the character provided in c"""
    n = len(s)
    print((n + 6) * c)
    print(c + '  ' + s + '  ' + c)
    print((n + 6) * c)


# ------------------------------------------------------------

if __name__ == '__main__':
    print_banner('Abracadabra')
    print_banner('Abracadabra', '#')
    print_banner('Abracadabra', c = '$')
