import string
import random

def generate_password(n_upper: int = 1,
                      n_lower: int = 1,
                      n_digits: int = 1,
                      n_special: int = 1,
                      min_length: int = 8) -> str:
    """This is my great password generator function. Use with CARE!"""

    n_extra = max(0, min_length - n_upper - n_lower - n_digits - n_special)

    upper = random.choices(string.ascii_uppercase, k = n_upper)
    lower = random.choices(string.ascii_lowercase, k = n_lower)
    digits = random.choices(string.digits, k = n_digits)
    special = random.choices('!@#$%&*()_+<>?/', k = n_special)
    extra = random.choices(string.ascii_uppercase + string.ascii_lowercase, k = n_extra)

    all = upper + lower + digits + special + extra

    random.shuffle(all)

    new_password = ''.join(all)

    return new_password


if __name__ == '__main__':
    print(help(generate_password))
    new_password = generate_password()
    print(f'Your new password is: {new_password}')

