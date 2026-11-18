import string
import random
import secrets


def exclude(s, characters_to_exclude="IlO.'`"):
    """Return a new string without the specified characters to exclude"""
    return list(filter(lambda item: item not in characters_to_exclude, s))


def choices(population, k=1, use_secrets=True):
    """Similar to random.choices but using the secrets library"""
    if use_secrets:
        return [secrets.choice(population) for _ in range(k)]
    else:
        return random.choices(population, k=1)


def generate_password(n_lower=1,
                      n_upper=1,
                      n_digits=1,
                      n_special=1,
                      n_length=8):
    """Generate a password"""

    n_extra = max(0, n_length - (n_lower + n_upper + n_digits + n_special))

    lower = choices(exclude(string.ascii_lowercase), k=n_lower)  # I l 1
    upper = choices(exclude(string.ascii_uppercase), k=n_upper)  # O 0
    digits = choices(exclude(string.digits), k=n_digits)
    special = choices(exclude(string.punctuation), k=n_special)
    extra = choices(exclude(string.ascii_letters), k=n_extra)

    all = lower + upper + digits + special + extra

    random.shuffle(all)

    password = ''.join(all)

    return password

