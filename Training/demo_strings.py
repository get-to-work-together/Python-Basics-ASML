name = 'Guido'
age = 62


print( name + ' is ' + str(age) + ' years old' )

print( name, 'is', age, 'years old' )

print( f'{name} is {age} years old' )

print( '{} is {} years old'.format(name, age) )


print( '%s is %d years old' % (name, age) )

import math
print( 'Pi is %.3f' % math.pi )
print( f'Pi is {math.pi:.3f}' )
