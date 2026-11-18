import string
import random
import secrets


n_lower = 1
n_upper = 1
n_digits = 1
n_special = 1
n_length = 8

n_extra = max(0, n_length - (n_lower + n_upper + n_digits + n_special))

def exclude(s, characters_to_exclude = "IlO.'`"):
    return list(filter(lambda item: item not in characters_to_exclude, s))

lower = random.choices(exclude(string.ascii_lowercase), k=n_lower)  # I l 1
upper = random.choices(exclude(string.ascii_uppercase), k=n_upper)  # O 0
digits = random.choices(exclude(string.digits), k=n_digits)
special = random.choices(exclude(string.punctuation), k=n_special)

extra = random.choices(exclude(string.ascii_letters), k=n_extra)

all = lower + upper + digits + special + extra

random.shuffle(all)

password = ''.join(all)

print('Your new password is:', password)

lower = [secrets.choice(string.ascii_lowercase) for _ in range(n_lower)]
upper = [secrets.choice(string.ascii_uppercase) for _ in range(n_upper)]
digits = [secrets.choice(string.digits) for _ in range(n_digits)]
special = [secrets.choice(string.punctuation) for _ in range(n_special)]

