from random import randint

user_choice = int(input("Pick a number 0-2: ")) 

if user_choice not in [0, 1, 2]:
    print("Your number is invalid. Please pick a number between 0 and 2.")
else:
    choices = ["Rock", "Paper", "Scissors"]
    print("Your choice is", choices[user_choice])

    computer_choice = randint(0, 2)
    print("Computer's choice is", choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")
