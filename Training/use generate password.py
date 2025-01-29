import sys

import passwords

# from passwords import generate_password

password = passwords.generate_password(6, 0, 0, 0)
print(f'Your new password is {password}')