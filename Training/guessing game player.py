import random

low = 1
high = 100

print('I will guess a number between {low} and {high}')
print('Please response with [h]igher, [l]ower or [y]es.')

number_of_guesses = 0
while True:
    guess = (low + high) // 2
    # guess = random.randint(low, high)

    response = input(f'Is your number: {guess}? ').lower()[0]
    number_of_guesses += 1

    if response == 'h':
        low = guess + 1

    elif response == 'l':
        high = guess - 1

    elif response == 'y':
        print(f'Great! I guessed the number in {number_of_guesses} guesses.')
        break

    if low > high:
        print('You cheated. I quit!')
        break