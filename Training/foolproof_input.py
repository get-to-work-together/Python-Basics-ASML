
def foolproof_input(lower=1, upper=10):
    while True:
        user_input = input(f'Enter a number between {lower} and {upper}: ')
        try:
            number = int(user_input)

            if lower <= number <= upper:
                break

            else:
                print(f'That number is not between {lower} and {upper}.')

        except ValueError:
            print(f'"{user_input}" is not a number.')

    return number

# -------------------------------------------------------------

if __name__ == '__main__':

    number = foolproof_input(1, 10)

    print(f'The number you entered ({number}) is OK.')