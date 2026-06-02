from passwords import generate_password
import passwords

print(passwords.generate_password())
print(generate_password(4, 4, 0, 0, min_length=8))
print(generate_password(n_digits=20, n_lower=0, n_upper=0, n_special=0, min_length=0))
print(generate_password(min_length=12, n_digits=0, n_special=0))