import string
import random


def generate_password_with_random_lengths():

    n_lowercase = random.randint(1, 4)
    n_uppercase = random.randint(1, 4)
    n_digits = random.randint(1, 2)
    n_punctuation = random.randint(1, 1)

    return generate_password(n_lowercase, n_uppercase, n_digits, n_punctuation)


def generate_password(n_lowercase: int = 1,
                      n_uppercase: int = 1,
                      n_digits : int = 1,
                      n_punctuation: int = 1) -> str:

    """Generate a password according to the specified numbers of characters per group"""

    lowercase = random.choices(string.ascii_lowercase, k = n_lowercase)
    uppercase = random.choices(string.ascii_uppercase, k = n_uppercase)
    digits = random.choices(string.digits, k = n_digits)
    punctuation = random.choices(string.punctuation, k = n_punctuation)

    all_characters = lowercase + uppercase + digits + punctuation

    random.shuffle(all_characters)

    password = ''.join(all_characters)

    return password


if __name__ == '__main__':

    password = generate_password(2, 4, 2, 1)
    print('Your new password is %s' % password)
