import string
import random

n_lower = 2
n_upper = 2
n_digits = 1
n_special = 1

minimal_length = 4

n_extra = max(minimal_length - (n_lower + n_upper + n_digits + n_special), 0)

lower = random.choices('abcdefghijkmnopqrstuvwxyz', k=n_lower) # removed l
upper = random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ', k=n_upper) # removed I, O
digits = random.choices(string.digits, k=n_digits)
special = random.choices('@#$%&*()', k=n_special)

extra = random.choices(string.ascii_letters, k=n_extra)

all = lower + upper + digits + special + extra

random.shuffle(all)

new_password = ''.join(all)

print('Your new password is: ' + new_password)


