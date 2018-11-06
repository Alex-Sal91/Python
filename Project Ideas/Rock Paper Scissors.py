from random import randint

player1_wins = 0
computer_wins = 0
winning_score = 3

while player1_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player1_wins}	Computer Score: {computer_wins}")
    print("...ROCK...")
    print("...PAPER...")
    print("...SCISSORS...")
    player_1 = input("Player 1 enter ROCK/PAPER/SCISSORS: ")
    player_1 = player_1.upper()

    random = randint(1, 3)
    if (random == 1):
        computer = "ROCK"
    elif (random == 2):
        computer = "PAPER"
    else:
        computer = "SCISSORS"
    print(f"Computer plays {computer}")

    if player_1 == computer:
        print("Tie!!")
    elif player_1 == "ROCK":
        if computer == "SCISSORS":
            print("Player 1 Won!!!")
            player1_wins += 1
        elif computer == "PAPER":
            print("Computer Won!!!")
            computer_wins += 1
    elif player_1 == "PAPER":
        if computer == "ROCK":
            print("Player 1 Won!!!")
            player1_wins += 1
        elif computer == "SCISSORS":
            print("Computer Won!!!")
            computer_wins += 1
    elif player_1 == "SCISSORS":
        if computer == "PAPER":
            print("Player 1 Won!!!")
            player1_wins += 1
        elif computer == "ROCK":
            print("Computer Won!!!")
            computer_wins += 1
    else:
        print("You chose an invalid selection!")

if player1_wins > computer_wins:
    print("CONGRATS, YOU WON!")
else:
    print("OH NO :( THE COMPUTER WON...")
print(f"Final Score: Player: {player1_wins} Computer: {computer_wins}")
