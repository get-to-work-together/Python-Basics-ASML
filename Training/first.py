print('Hello world')
print("Hello world")

name = input('Enter your name: ')

print('Hello', name)              # !!! NOT IN PYTHON 2
print('Hello ' + name)
print('Hello %s' % name)
print('Hello {}'.format(name))
print(f'Hello {name}')            # !!! NOT IN PYTHON 2

# print 'Hello %s' % name           PYTHON 2! NOT IN PYTHON 3!!!

print(len(name))