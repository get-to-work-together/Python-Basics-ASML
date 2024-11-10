def print_goodmorning(name: str):
    print('Goodmorning %s' % name)


def calculate_bmi(weight: float|int, height: float|int) -> float:
    bmi = weight / height ** 2
    return bmi



if __name__ == '__main__':

    print_goodmorning('Peter')
    print_goodmorning('Arthur')
    print_goodmorning(9087)


    print( calculate_bmi(98, 1.85) )
