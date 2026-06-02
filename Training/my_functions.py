def print_banner(text, c = '*'):
    n = len(text) + 6
    print(c * n)
    print(f'{c}  {text}  {c}')
    print(c * n)


# -------------------------------------------------

if __name__ == '__main__':
    print_banner('Peter')
    print_banner('ABRACADABRA', '#')
    print_banner('Nadia', '$')

