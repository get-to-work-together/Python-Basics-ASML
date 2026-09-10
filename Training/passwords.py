import string
import random


def create_password(n_lower = 1,
                    n_upper = 1,
                    n_digits = 1,
                    n_special = 1,
                    n_length = 8):

    n_extra = max(0, n_length - (n_lower + n_upper + n_digits + n_special))

    lower = random.choices(string.ascii_lowercase, k=n_lower)  # I 1 l
    upper = random.choices(string.ascii_uppercase, k=n_upper)  # O 0
    digits = random.choices(string.digits, k=n_digits)
    special = random.choices('!@#$%^&*(){}[]_-+=:;<>,.?/', k=n_special)

    extra = random.choices(string.ascii_letters, k=n_extra)

    all = lower + upper + digits + special + extra

    random.shuffle(all)

    password = ''.join(all)

    return password


# ----------------------------------------------------------

if __name__ == '__main__':
    password = create_password(1, 1, 0, 0, 20)
    print(password)
