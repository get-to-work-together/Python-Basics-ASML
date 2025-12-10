
def banner(content, c: str = '*') -> None:
    s = str(content)
    n = len(s)
    print((n + 6) * c)
    print(f'{c}  {s}  {c}')
    print((n + 6) * c)



# ----------------------------------------------------

banner('Abracadabra')
banner('Abracadabra', c='#')
banner('Abracadabra', c='$')
banner('Abracadabra', c='❤️')
banner('Abracadabra', c='😁')

banner(82389, c='#')

