
def show_arguments(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'Number of positional arguments {len(args)}')
    print(f'Number of keyword arguments {len(kwargs)}')


# ---------------------------------------------------

show_arguments(2, 5, 7)
show_arguments('A', 'B', 'C')
show_arguments(3, 6, factor = 0.7)

settings = {
    'offset': 10,
    'factor': 2.5,
    'frequency': 440
}

show_arguments(**settings)