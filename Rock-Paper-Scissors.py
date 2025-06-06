import random

print("Welcome to Rock, Paper, Scisssor")
print("..........\n")
print("How to play: ")
print("Input Rock or Paper or Scissors and find out the if you win or lose ")
print("Your opponent is the computer good luck")
print("..................\n")

import random

def play_game(player_move):
    options = ["rock", "paper", "scissors"]
    player_move = player_move.lower()

    if player_move not in options:
        raise ValueError(f"{player_move} is not a valid move. Choose from {options}")

    computer_move = random.choice(options)
    print(f"Computer chose: {computer_move}")

    if computer_move == player_move:
        print("It's a tie! 👔")
    elif computer_move == "rock":
        if player_move == "paper":
            print("You win, paper wraps the rock! ")
        else:
            print("You lose.. rock beats scissors! ")
    elif computer_move == "paper":
        if player_move == "rock":
            print("You lose.. paper wraps the rock! ")
        else:
            print("You win, scissors cut the paper! ")
    else:  # computer_move == "scissors"
        if player_move == "paper":
            print("You lose.. scissors cut the paper!")
        else:
            print("You win, rock breaks the scissors!")

while True:
    player_input = input("Please enter your move (rock, paper, or scissors): ").strip().lower()
    try:
        play_game(player_input)
    except ValueError as e:
        print(e)
        continue

    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

