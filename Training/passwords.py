import string
import random
import doctest


def generate_password(n_lower: int = 1,
                      n_upper: int = 1,
                      n_digits: int = 1,
                      n_special: int = 1,
                      length: int = 8) -> str:
    """Generate a password following the given requirements

    # >>> len(generate_password())
    # 8
    #
    # >>> len(generate_password(length=10))
    # 10
    """

    assert length > 0, "length must be positive!!!"

    n_extra = max(length - n_lower - n_upper - n_digits - n_special, 0)

    lower = random.choices('abcdefghijkmnopqrstuvwxyz', k=n_lower)
    upper = random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ', k=n_upper)
    digits = random.choices(string.digits, k=n_digits)
    special = random.choices(string.punctuation, k=n_special)

    extra = random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = n_extra)

    all = lower + upper + digits + special + extra

    random.shuffle(all)

    password = ''.join(all)

    return password

# ----------------------------------------------------------

if __name__ == '__main__':

    # doctest.testmod(verbose=True)

    password = generate_password()
    print(f'You new password is {password}')

    password = generate_password(length = 20)
    print(f'You new password is {password}')

    # password = generate_password(length = -1)
    # print(f'You new password is {password}')