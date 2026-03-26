from passwords import generate_password

print('Your new password is:', generate_password())
print('Your new password is:', generate_password(n_upper = 4, n_lower = 4, n_digits = 0, n_special = 0))
print('Your new password is:', generate_password(n_upper = 0, n_lower = 0, n_digits = 10, n_special = 0))
