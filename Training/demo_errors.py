
# n = 0
# print(1/n)

# numbers = [1,2,3]
# print( numbers[3] )


try:
    user_input = input('Give a number: ')
    print( int(user_input) )

except:
    print('That is not a number')


filename = 'whatever.txt'
with open(filename) as f:
    f.read()

