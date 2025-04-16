import string
import random

n_lowercase = 2
n_uppercase = 2
n_digits = 2
n_special = 1

lowercase = random.choices(string.ascii_lowercase, k = n_lowercase)
uppercase = random.choices(string.ascii_uppercase, k = n_uppercase)
digits = random.choices(string.digits, k = n_digits)
special = random.choices(string.punctuation, k = n_special)

all = lowercase + uppercase + digits + special

random.shuffle(all)

password = ''.join(all)

print('Your new password is:', password)