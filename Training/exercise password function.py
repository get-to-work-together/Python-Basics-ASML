from passwords import generate_password

password = generate_password()
password = generate_password(4, 4, 0, 0)
password = generate_password(0, 0, 8, 0)

print('Your new password is:', generate_password())
print('Your new password is:', generate_password(4, 4, 0, 0))
print('Your new password is:', generate_password(0, 0, 8, 0, n_length=10))