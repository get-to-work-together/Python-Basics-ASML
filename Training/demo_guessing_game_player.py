print(f'I will try to guess a number between 1 and 100')

lower = 1
upper = 100
number_of_guesses = 0
while True:
    guess = (lower + upper) // 2
    response = input(f'Is your number {guess}? : [l/h/y] ').lower()
    number_of_guesses += 1

    if response.startswith('l'):
        upper = guess - 1
    elif response.startswith('h'):
        lower = guess + 1
    elif response.startswith('y'):
        print(f'Yeah! Guessed it in {number_of_guesses} guesses!')
        break
    else:
        print('Invalid input. Try again.')

    if lower > upper:
        print('That\'s impossible! You cheated. I quit.')
        break
