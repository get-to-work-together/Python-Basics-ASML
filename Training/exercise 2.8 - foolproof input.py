def foolproof_input(prompt, lower, upper):
    while True:
        try:
            user_input = input(prompt)

            if user_input:
                number = int(user_input)
            else:
                print('Please enter a number.')
                continue

            if lower <= number <= upper:
                return number

            else:
                print(f'The number you entered "{number}" is not between {lower} and {upper}.')
                continue

        except ValueError:
            print(f'"{user_input}" is not a number.')
            continue

        except KeyboardInterrupt:
            print('\nOK. Stopping now.')
            break


number = foolproof_input('Enter a number between 1 and 10: ', 1, 10)

if number is not None:
    print(f'Thank you. You entered the number "{number}".')
