
def print_banner(name, c = '*'):
    n = len(name)
    print((n + 6) * c)
    print(f'{c}  {name}  {c}')
    print((n + 6) * c)

# -------------------------------------------------------

print_banner('Peter')
print_banner('Peter', '#')

print_banner('Peter', c = '$')

