import string
import random

n_upper = 3
n_lower = 3
n_digits = 1
n_special = 1

lower = random.choices(string.ascii_lowercase, k = n_upper)
upper = random.choices(string.ascii_uppercase, k = n_lower)
digits = random.choices(string.digits, k = n_digits)
special = random.choices(string.punctuation, k = n_special)

all = lower + upper + digits + special

random.shuffle(all)

password = ''.join(all)

print('Your new password is ' + password)
print('Your new password is %s' % password)
print('Your new password is {}'.format(password))
print(f'Your new password is {password}')
