import math

user_input = input('Give the radius of a circle: ')

r = float(user_input)

area = math.pi * r ** 2
circumference = 2 * math.pi * r

print('Radius: ' + str(r))
print('Area: ' + str(area))
print('Circumference: ' + str(circumference))

print('Radius:', r)
print('Area:', area)
print('Circumference:', circumference)

print( f'Radius: {r:.3f}' )
print( f'Area: {area:.3f}' )
print( f'Circumference: {circumference:.3f}' )

print( 'Radius: %.3f' % r)
print( 'Area: %.3f' % area)
print( 'Circumference: %.3f' % circumference)

print( 'Radius: {:.3f}'.format(r))
print( 'Area: {:.3f}'.format(area))
print( 'Circumference: {:.3f}'.format(circumference))
