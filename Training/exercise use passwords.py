import passwords

settings = {'n_lower': 1,
            'n_upper': 1,
            'n_digits': 0,
            'n_special': 0,
            'n_length': 20}

password = passwords.create_password(**settings)

print(password)
