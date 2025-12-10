
def foolproof_input(prompt: str, lower: int, upper: int) -> int | None:
    """Ask the user to input a number between two bounds and correctly handle wrong input."""

    while True:
        try:
            user_input = input(prompt)

            if user_input == '':
                print('Nothing was entered.')
                continue

            number = int(user_input)

            if lower <= number <= upper:
                return number
            else:
                print(f'{number} is not between {lower} and {upper}.')

        except ValueError:
            print(f'"{user_input}" is not a number.')

        except KeyboardInterrupt:
            print('\nOK. Stoping now.')
            return None


# ----------------------------------------------------------------

if __name__ == '__main__':

    lower = 1
    upper = 10
    number = foolproof_input(f'Give me a number between {lower} and {upper}: ',
                             lower,
                             upper)

    if number is not None:
        print('The number you entered (%d) is OK' % number)
