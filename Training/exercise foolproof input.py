
def foolproof_input(prompt, lower, upper):
    while True:
        try:
            user_input = input(prompt)

            number = int(user_input)

            if number < lower:
                print(f'The number "{number}" is too small')

            elif number > upper:
                print(f'The number "{number}" is too large')

            else:
                return number

        except ValueError:
            print(f'"{user_input}" is not a number')


# --------------------------------------------

if __name__ == '__main__':
    number = foolproof_input('Give me a number: ', 1, 10)
    print(f'The number you entered was: {number}')