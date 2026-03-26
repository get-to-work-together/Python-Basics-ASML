def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)


def print_goodmorning(name):
    print('\nGoodmorning %s' % name)


# ----------------------------------------------------------
# Usage (i.e. client code)

book_flight('BRS', 'VER', 2, 2)
book_flight('LHR', 'VIE', 4)
book_flight('LHR', 'OSL')
book_flight(toairport = 'LHR', fromairport = 'OSL', numadults = 5)


name = 'Peter' # global
print_goodmorning(name)
