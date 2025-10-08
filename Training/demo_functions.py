def print_goodmorning(name, n=1):
    for _ in range(n):
        print(f'Goodmorning {name}')
    print('How are you today?')
    print('Have a great day!')


def calculate_bmi(weight: int|float, height: int|float) -> float:
    bmi = weight / height ** 2
    return bmi, weight, height


def ask_and_print_bmi():
    weight = float(input('Weight: '))
    height = float(input('Height: '))
    bmi, *_ = calculate_bmi(weight, height)
    print(f'Your BMI is {bmi:.1f}')


def book_flight(fromairport: str,
                toairport: str,
                numadults: int = 1,
                numchildren: int = 0) -> None:
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)


def do_something(a=None):
    if a is None:
        a = 3
    return a * 100

do_something()

# ----------------------------------------------------

# print_goodmorning('Peter')
# print_goodmorning('Jan', 6)
#
# bmi, *_ = calculate_bmi(80, 1.80)
# print(bmi)
#
# ask_and_print_bmi()


book_flight('AMS', 'LHR', 2, 2)
book_flight('AMS', 'LHR', 2)
book_flight('AMS', 'LHR')

book_flight(toairport='LHR', fromairport='AMS')
book_flight(toairport='LHR', fromairport='AMS', numchildren=10)

book_flight('AMS', 'LHR', numchildren=10)
