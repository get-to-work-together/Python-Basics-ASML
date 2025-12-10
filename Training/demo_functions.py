
def print_goodmorning(name: str = 'stranger'):
    """This function will print a welcome message."""

    # printing to stdout
    print(f'Goodmorning {name}')
    print('How are you today?')
    print('Have a great day!')


def calculate_bmi(weight: int|float, height: int|float) -> float:
    bmi = weight / height ** 2
    return bmi


def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)

    

# --------------------------------------------------

print_goodmorning('Alexandra')
print_goodmorning('Deeksha')
print_goodmorning()

weight = 85
height = 1.75

my_bmi = calculate_bmi(weight, height)


print(f'The bmi is {my_bmi}')


book_flight('AMS', 'LHR', 2, 4)
book_flight('AMS', 'LHR', 2)
book_flight('AMS', 'LHR')

book_flight('AMS', 'LHR', numchildren=10)
book_flight('AMS', 'LHR', numchildren=10, numadults=2)

book_flight(numchildren=10, numadults=2, fromairport='AMS', toairport='LHR')
