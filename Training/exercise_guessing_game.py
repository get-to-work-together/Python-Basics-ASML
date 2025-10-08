import random

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

number_of_guesses = 0
for _ in range(10):
    guess = int(input('What do you think the number is? : '))
    number_of_guesses += 1

    if guess > secret_number:
        print('lower ...')

    elif guess < secret_number:
        print('higher')

    else:
        print(f'YEAAHHH! The number was {secret_number}. You guessed it in {number_of_guesses} guesses.')
        break

else:
    print('Maximum number of guesses. Game over!')
