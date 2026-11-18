
def create_banner(name, c = '*'):
    """This is my banner function

    Your text will be surrounded by a specified character.
    """
    n = len(name)
    lines = []
    lines.append((n + 6) * c)
    lines.append(f'{c}  {name}  {c}')
    lines.append((n + 6) * c)
    return '\n'.join(lines)


def print_banner(name, c = '*'):
    """Prints the result of create_banner"""
    print(create_banner(name, c))


# ----------------------------

if __name__ == '__main__':

    print(create_banner('Peter', '+'))