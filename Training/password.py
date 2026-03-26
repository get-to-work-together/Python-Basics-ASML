import string
import random

n_upper = 3
n_lower = 3
n_digits = 2
n_special = 1

lower = random.choices(string.ascii_lowercase, k = n_upper)
upper = random.choices(string.ascii_uppercase, k = n_lower)
digits = random.choices(string.digits, k = n_digits)
punctuation = random.choices('&$#@!?', k = n_special)

all = lower + upper + digits + punctuation

random.shuffle(all)

new_password = ''.join(all)

print('Your new password is:', new_password)
