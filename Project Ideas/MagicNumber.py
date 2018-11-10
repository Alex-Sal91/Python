import random

magic_number = random.randint(1,101)

def Play():
    count = 0
    guess = raw_input("Enter a number between 1 and 100: ")
    while guess != magic_number and count < 4:
        print("Wrong guess...Try Again!")
        guess = raw_input("Enter a number between 1 and 100: ")
        count += 1
    if guess == magic_number:
        print('Congrats! You guessed correct!')
    else:
        print("You're out of guesses!")
        print("The magic number was {}".format(magic_number))


Play()