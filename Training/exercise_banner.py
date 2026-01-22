def print_banner(text: str) -> None:
    """Print a banner"""
    n = len(text)
    print((n + 6) * '*')
    print('*  ' + text + '  *')
    print((n + 6) * '*')


def create_banner(text: str, c: str = '*') -> str:
    """Create a banner"""
    n = len(text)
    lines = []
    lines.append((n + 6) * c)
    lines.append(c + '  ' + text + '  ' + c)
    lines.append((n + 6) * c)
    return '\n'.join(lines)

def print_banner(text: str, *args, **kwargs) -> None:
    print(create_banner(text, *args, **kwargs))


# ------------------------------------------------------------

if __name__ == '__main__':
    print_banner('Peter')
    print_banner('Abracadabra', c='#')
