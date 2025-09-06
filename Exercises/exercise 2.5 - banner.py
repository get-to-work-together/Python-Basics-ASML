
def banner(text):
    n = len(text)
    print('***' + '*' * n + '***')
    print('*  ' + text    + '  *')
    print('***' + '*' * n + '***')


def banner(text, c = '*'):
    n = len(text)
    print(c * (n + 6))
    print(f'{c:<3}{text}{c:>3}')
    print(c * (n + 6))








# def box(text):
#     """Create the text in a box using unicode box characters"""
#     n = len(text)
#     s  = '┏━━' + '━' * n + '━━┓\n'
#     s += '┃  ' + text + '  ┃\n'
#     s += '┗━━' + '━' * n + '━━┛'
#     return s



# def create_banner(text: str, c: str = '*', max_length: int = None) -> str:
#     """A more generic function to create a banner
#
#     arguments:
#        text - the text to put in the banner
#        c - the surrounding character. Default = '*'
#        max_length - the maximal length of the banner. Default = no limit"""
#
#     if max_length is None:
#         n = len(text)
#     else:
#         n = max_length - 6
#         text = text[:n-3] + '...'
#
#     s  = c * (n + 6) + '\n'
#     s += c + '  ' + text + '  ' + c + '\n'
#     s += c * (n + 6)
#     return s


# def print_banner(text: str, **kwargs):
#     """Print the created banner"""
#     print(create_banner(text, **kwargs))


# ----------------------------------------------------------

if __name__ == '__main__':

    name = input('What is your name? : ')

    banner(name)
    banner(name, '#')
    banner(name, c='☆')
