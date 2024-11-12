
def calculate_cube(number):
    cube = number ** 3
    return cube

def say_hi(name = 'Stranger'):
    print('Hi %s!' % name)
    print('How do you do?')
    print('Bye')


say_hi('Peter')
say_hi()

print( calculate_cube(2) )
print( calculate_cube(20) )

