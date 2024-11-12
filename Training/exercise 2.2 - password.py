import string
import random

n_lowercase = random.randint(1, 4)
n_uppercase = random.randint(1, 4)
n_digits = random.randint(1, 2)
n_punctuation = random.randint(1, 1)

lowercase = random.choices(string.ascii_lowercase, k = n_lowercase)
uppercase = random.choices(string.ascii_uppercase, k = n_uppercase)
digits = random.choices(string.digits, k = n_digits)
punctuation = random.choices(string.punctuation, k = n_punctuation)

all_characters = lowercase + uppercase + digits + punctuation

random.shuffle(all_characters)

password = ''.join(all_characters)

print('Your new password is %s' % password)
