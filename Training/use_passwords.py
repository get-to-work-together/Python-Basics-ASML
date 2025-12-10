import passwords

password = passwords.generate_password()
print(f'You new password: {password}')

password = passwords.generate_password(n_upper=20, 
                                      n_lower=0, 
                                      n_digits=0, 
                                      n_special=0, 
                                      length = 20)
print(f'You new password: {password}')