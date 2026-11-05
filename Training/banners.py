
def create_banner(text: str, c: str = '*') -> str:
    """Creates a banner of stars around the text"""
    n = len(text)
    lines = []
    lines.append((n + 6) * c)
    lines.append(c + '  ' + text + '  ' + c)
    lines.append((n + 6) * c)
    return '\n'.join(lines)

def print_banner(*args, **kwargs):
    """Print a banner of stars around the text"""
    print(create_banner(*args, **kwargs))


# -------------------------------------------------------

if __name__ == '__main__':
    print_banner('Peter')
    print_banner('Abracadabra', '#')
    print_banner('WINNER', c = '$')