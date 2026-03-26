
def foolproof_input(prompt, lower, upper):
    while True:
        try:
            user_input = input(prompt)
            if user_input == '':
                print('You did not enter anything')
                continue

            number = int(user_input)
            if lower <= number <= upper:
                return number
            else:
                print('{} is not between {} and {}'.format(number, lower, upper))
                continue

        except ValueError:
            print('"{}" is not a number'.format(user_input))
            continue


# -----------------------------------------------------------

number = foolproof_input('Enter a number between 1 and 10: ', 1, 10)
print('The number you entered is {}'.format(number))