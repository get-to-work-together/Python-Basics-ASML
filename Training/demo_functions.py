
def print_goodmorning(name: str = 'Stranger'):
    def fix_name(name):
        return name.title().strip()
    print(f'Goodmorning {fix_name(name)}')
    print('How are you today?')
    print('Have a great day!')


def calculate_sum_and_factor(a: int|float, b: int|float, factor: int|float = 1) -> int|float:
    """Calculate the sum of a and b and multiply by a factor"""
    result = (a + b) * factor
    return result

# ---------------------------------------------------

if __name__ == '__main__':

    print_goodmorning()

    names = ['Joost', 'Peter', 'Vuyas']

    for name in names:
        print_goodmorning(name)

    a = 7
    b = 9
    f = 19
    result = calculate_sum_and_factor(a, b, f)
    print(result)

    print(calculate_sum_and_factor(a, b, factor=3))