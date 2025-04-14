while True:

    UserText = input('enter text : ')

    if len(UserText) != 0:

        PUserText = UserText.upper()

        print(f'UPPER CASE {PUserText}')

        print(f'lower case {UserText.lower()}')

        print(f'lower case {UserText[:4]}')

    else:
        break
