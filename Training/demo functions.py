
def print_goodmorning(name, n = 1):
    for _ in range(n):
        print('Goodmorning ' + name)
    print('How are you today?')
    print('Have a great day!')


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi


def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)


# ----------------------------------------------------------

if __name__ == '__main__':

    print_goodmorning('Peter')
    print_goodmorning('Peter', 1)
    print_goodmorning('Max', 2)
    print_goodmorning('Sophia', 3)

    bmi = calculate_bmi(99, 1.80)
    print(bmi)

    book_flight('BRS', 'VER', 2, 2)
    book_flight('LHR', 'VIE', 4)
    book_flight('LHR', 'OSL')

    book_flight(fromairport='LHR', toairport='OSL', numchildren=12)
    book_flight(numchildren=12, toairport='OSL', fromairport='LHR')

    book_flight('LHR', 'OSL', numchildren=12)

