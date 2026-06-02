def print_banner(text:str, c:str='*') -> None:
    n = len(text) + 6
    print(c * n)
    print(f'{c}  {text}  {c}')
    print(c * n)


# -------------------------------------------------

print_banner('Peter')
print_banner('ABRACADABRA', '#')
print_banner('Nadia', '$')

