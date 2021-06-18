import random


def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while random_number != user_guess:
        user_guess = int(input(f'Guess a number between 1 and {x}: '))
        print(user_guess)
        if (user_guess < random_number):
            print(f'Sorry, guess again.Too Low.')
        elif (user_guess > random_number):
            print(f'Sorry, guess again.Too High')
    print(f'Yay! you guessed the number right')


def guess_computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback.lower() != 'c':
        if high != low:
            computers_guess = random.randint(low, high)
        else:
            computers_guess = low
        feedback = input(f'Is {computers_guess} to High (H), too Low (L) or Correct (C)')
        if feedback.lower() == 'h':
            high = computers_guess - 1
        elif feedback.lower() == 'l':
            low = computers_guess + 1
    print(f'That was fun')


if __name__ == '__main__':
    # guess(10)
    guess_computer(1000)
