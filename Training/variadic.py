

def generic_function(*args, **kwargs):
    print(args)
    print(kwargs)

generic_function(1, 2, 3, 4)
generic_function(1, a=2, b=3, c=4)
generic_function(1, 2, 3, x=4)