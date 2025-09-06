
def foolproof_input(prompt: str, lower: int, upper: int) -> int | None:
    """Ask the user to input a number between two bounds and correctly handle wromg input."""

    while True:
        try:
            response = input(prompt)

            if response == '':
                print('Nothing was entered.')
                continue

            number = int(response)

            if lower <= number <= upper:
                return number
            else:
                print(f'{number} is not between {lower} and {upper}.')

        except ValueError:
            print(f'"{response}" is not a number.')

        except KeyboardInterrupt as ex:
            print('\nOK. Stoping now.')
            return


# ----------------------------------------------------------------

if __name__ == '__main__':

    lower = 1
    upper = 10
    number = foolproof_input(f'Give me a number between {lower} and {upper}: ', lower, upper)

    if number is not None:
        print('The number you entered (%d) is OK' % number)
