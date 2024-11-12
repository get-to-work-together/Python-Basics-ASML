from password import generate_password

password = generate_password(2, 4, 2, 1)
print('Your new password is %s' % password)