
def foolproof_input(prompt, lower_bound, upper_bound):
    while True:
        user_input = input(prompt)

        try:
            number = int(user_input)

            if lower_bound <= number <= upper_bound:
                return number

            else:
                print(f'The number {number} is not between {lower_bound} and {upper_bound}. Please try again.')

        except ValueError:
            print(f'"{user_input}" is not a number. Please try again.')


# -------------------------------------------------------------

if __name__ == '__main__':

    number = foolproof_input('Give a number between 1 and 10: ', 1, 10)

    print(f'The number you entered ({number}) is OK.')