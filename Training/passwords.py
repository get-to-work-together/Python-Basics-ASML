import string
import random


def generate_password(n_upper = 3,
                      n_lower = 3,
                      n_digits = 1,
                      n_special = 1):

    lower = random.choices(string.ascii_lowercase, k=n_upper)
    upper = random.choices(string.ascii_uppercase, k=n_lower)
    digits = random.choices(string.digits, k=n_digits)
    special = random.choices(string.punctuation, k=n_special)

    all = lower + upper + digits + special

    random.shuffle(all)

    password = ''.join(all)

    return password


# -------------------------------------------------------

if __name__ == '__main__':

    password = generate_password()
    print(password)

    print(generate_password(5, 5, 0, 0))
    print(generate_password(n_upper = 0, n_lower = 0, n_digits = 8, n_special = 0))
