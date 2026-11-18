
def foolproof_input(prompt, lower, upper, stop_if_no_input = False):
    while True:
        try:
            user_input = input(prompt)

            if user_input == '':
                if stop_if_no_input:
                    print('Exiting')
                    return ''
                else:
                    print(f'No input')
                    continue

            number = int(user_input)

            if number < lower:
                print(f'The number "{number}" is too small')

            elif number > upper:
                print(f'The number "{number}" is too large')

            else:
                return number

        except ValueError:
            print(f'"{user_input}" is not a number')

        except KeyboardInterrupt:
            print('\nExiting')
            return ''


# --------------------------------------------

if __name__ == '__main__':
    number = foolproof_input('Give me a number: ', 1, 10)
    if number:
        print(f'The number you entered was: {number}')