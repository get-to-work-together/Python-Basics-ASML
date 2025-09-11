import random


def print_goodmorning(name, n):
    for _ in range(n):
        print(f'Goodmorning {name}')
    print('Have a good one.')


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi


def ask_and_calculate_bmi():
    weight = float(input('What is your weight [kg]? : '))
    height = float(input('What is your height [m]? : '))
    calculated_bmi = calculate_bmi(weight, height)
    return calculated_bmi


def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)


# =============================================================

# names = ['Aranaf', 'Chun', 'James']
#
# name: str = random.choice(names)
# print_goodmorning(name, 2)


# weight = float(input('What is your weight [kg]? : '))
# height = float(input('What is your height [m]? : '))
# calculated_bmi = calculate_bmi(weight, height)
# print(calculated_bmi)


book_flight('AMS', 'DEN', 1, 0)
book_flight('AMS', 'DEN', 1)
book_flight('AMS', 'DEN')

book_flight('AMS', 'DEN', numchildren=2)
book_flight('AMS', 'DEN', numchildren=2, numadults=4)
book_flight(toairport='DEN', numchildren=2, numadults=4, fromairport='AMS')


