
def print_goodmorning(name, k=1):
    for _ in range(k):
        print('Goodmorning', name)
    print('How are you today?')
    print('Have a great day!')


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi

# -------------------------------------------------

print_goodmorning('Olec')
print_goodmorning('Giudo', k=2)

print(calculate_bmi(97, 1.80))
