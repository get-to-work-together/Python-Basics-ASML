"""Module demo

Written by Peter Anema

History:
"""
def calculate_bmi(weight: float|int, height: float|int) -> float:
    """Calculate BMI based on weight, height.

    Params:
    weight (float|int): Weight in kg
    height (float|int): Height in cm
    """
    bmi = weight / height ** 2
    return bmi


def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)


def return_both(a, b):
    return a + b, a - b




height = float(input('What is your height? '))
weight = int(input('What is your weight? '))
result = calculate_bmi(weight, height)
print(f'Your BMI is {result}')


print(return_both(6, 4))

