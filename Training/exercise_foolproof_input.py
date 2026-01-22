
def foolproof(prompt: str, lower: int, upper: int) -> int|None:
    while True:
        try:
            user_input = input(prompt).strip()

            if user_input == '':
                print(f'You need to enter a number between {lower} and {upper}.')
                continue

            value = int(user_input)

        except ValueError:
            print(f'"{user_input}" is not a valid number')
            continue

        except KeyboardInterrupt:
            return None

        if lower <= value <= upper:
            return value

        else:
            print(f'{value} is not between {lower} and {upper}.')
            continue


# ============================================================

if __name__ == '__main__':
    number = foolproof('Give me a number between 1 and 10: ', 1, 10)
    if number is None:
        print(f'Nothing was entered!')
    else:
        print(f'The number you entered was {number}')