import random
import string


def generate_password(n_lower: int = 2,
                      n_upper: int = 2,
                      n_digits: int = 1,
                      n_special: int = 1,
                      minimal_length: int = 8) -> str:
    """Generate a random password"""

    n_extra = max(minimal_length - (n_lower + n_upper + n_digits + n_special), 0)

    lower = random.choices('abcdefghijkmnopqrstuvwxyz', k=n_lower)  # removed l
    upper = random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ', k=n_upper)  # removed I, O
    digits = random.choices(string.digits, k=n_digits)
    special = random.choices('@#$%&*()', k=n_special)

    extra = random.choices(string.ascii_letters, k=n_extra)

    all_characters = lower + upper + digits + special + extra

    random.shuffle(all_characters)

    return ''.join(all_characters)


# ---------------------------------------------------------------------

if __name__ == '__main__':

    password = generate_password()
    print('Your new password is: ' + password)

    password = generate_password(minimal_length=12)
    print('Your new password is: ' + password)

    password = generate_password(n_lower=6, n_upper=6, n_digits=0, n_special=0)
    print('Your new password is: ' + password)

    password = generate_password(n_lower=0, n_upper=0, n_digits=20, n_special=0)
    print('Your new password is: ' + password)
