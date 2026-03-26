import string
import random

def generate_password(n_upper: int = 3,
                      n_lower: int = 3,
                      n_digits: int = 2,
                      n_special: int = 1) -> str:
    """Genreate a random password with the requirements specified."""

    lower = random.choices(string.ascii_lowercase, k=n_upper)
    upper = random.choices(string.ascii_uppercase, k=n_lower)
    digits = random.choices(string.digits, k=n_digits)
    punctuation = random.choices('&$#@!?', k=n_special)

    all = lower + upper + digits + punctuation

    random.shuffle(all)

    new_password = ''.join(all)

    return new_password



# ---------------------------------------------------------------

if __name__ == '__main__':
    password = generate_password()
    print('Your new password is:', password)