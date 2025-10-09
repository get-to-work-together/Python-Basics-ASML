import random
import string


def generate_password(min_length = 8,
                      n_lower = 1,
                      n_upper = 1,
                      n_digits = 1,
                      n_special = 1):

    n_extra = max(0, min_length - n_lower - n_upper - n_digits - n_special)

    lower = random.choices(string.ascii_lowercase, k=n_lower)
    upper = random.choices(string.ascii_uppercase, k=n_upper)
    digits = random.choices(string.digits, k=n_digits)
    special = random.choices(string.punctuation, k=n_special)
    extra = random.choices(string.ascii_letters, k=n_extra)

    all = lower + upper + digits + special + extra

    random.shuffle(all)

    return ''.join(all)


# -----------------------------------------------------

if __name__ == '__main__':

    print( generate_password() )
    print( generate_password(min_length = 10,
                             n_lower = 0,
                             n_upper = 10,
                             n_digits = 0,
                             n_special = 0) )
