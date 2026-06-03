
def say_hi(name):
    print(f'Hi {name}!')

def say_goodbye(name):
    print(f'Bye {name}!')

# ---------------------------------

print(type(say_hi))

say_hi('Nadia')

list_of_functions = [say_hi, say_goodbye]

list_of_functions[0]('Hakan')

name = 'Jochem'
for f in list_of_functions:
    f(name)