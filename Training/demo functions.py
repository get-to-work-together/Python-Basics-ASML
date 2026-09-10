
def print_goodmorning(name: str):
    print('Goodmorning', name)
    print('How are you today?')
    print('Have a great day!')


def calculate_bmi(weight: int|float, height: int|float) -> float:
    bmi = weight / height ** 2
    return bmi, weight, height


def book_flight(fromairport: str, toairport: str, numadults: int=1, numchildren:int=0):
    """This is my booking function"""
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)

# ------------------------------------------------------------

print_goodmorning(897)
print_goodmorning('Barend')

bmi, *_ = calculate_bmi(90, 1.80)
print(bmi)


book_flight('AMS', 'LHR', 2, 2)
book_flight('AMS', 'LHR', 2)
book_flight('AMS', 'LHR')

book_flight(fromairport = 'AMS', toairport = 'LHR', numadults = 5, numchildren = 3)
book_flight(numchildren = 3, toairport = 'LHR', numadults = 5, fromairport = 'AMS')
book_flight('AMS', 'LHR', numchildren = 3)

print(help(book_flight))