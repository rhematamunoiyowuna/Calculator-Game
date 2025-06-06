import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

word_list = ['spain', 'japan', 'sudan', 'niger', 'malta', 
             'egypt','apple', 'grape', 'mango', 'pearl', 'stone', 
             'brave', 'flame', 'drink', 'fresh', 'video', 'wheel',
             'plane', 'fruit', 'lemon', 'poise', 'actor', 'earth',
             'house', 'field','green', 'travel', 'house', 'stamp',
             'nurse', 'climb','habit','plant', 'water', 
] 
print("Welcome to Wordle! Guess the 5-letter word.\n")
print("Here's how to play wordle")

sample_list = []
sample_word = "APPLE"
comparing_word = "ALLEN"

for i in range(len(sample_word)):
    letter = sample_word[i]
    
    if letter == comparing_word[i]:
        sample_list.append(Back.GREEN + Fore.BLACK + f" {letter} " + Style.RESET_ALL)
    elif letter in comparing_word:
        sample_list.append(Back.YELLOW + Fore.BLACK + f" {letter} " + Style.RESET_ALL)
    else:
        sample_list.append(Back.LIGHTBLACK_EX + Fore.WHITE + f" {letter} " + Style.RESET_ALL)

print("".join(sample_list))


print("'A' is in the word and in the correct spot")
print("'P' and 'P' are not in the word")
print("'L' and 'E' are in the word but in the wrong spot")
print(".................................\n")


def play_wordle():
    Wordle = random.choice(word_list)
    max_attempts = 6
    

    for attempt in range(max_attempts):
        while True:
            guess = input(f"Attempt {attempt + 1}/{max_attempts}: ").lower()
            if len(guess) == 5 and guess.isalpha():
                break
            print(Fore.RED + "Word not in list!")

    
        feedback = []
        for i in range(len(Wordle)):
            letter = guess[i].upper()
            if guess[i] == Wordle[i]:
                feedback.append(Back.GREEN + Fore.BLACK + f" {letter} " + Style.RESET_ALL)
            elif guess[i] in Wordle:
                feedback.append(Back.YELLOW + Fore.BLACK + f" {letter} " + Style.RESET_ALL)
            else:
                feedback.append(Back.LIGHTBLACK_EX + Fore.WHITE + f" {letter} " + Style.RESET_ALL)

        print("".join(feedback))

        if guess == Wordle:
            print(Fore.BLUE + f"\n You got it {Wordle.upper()}.")
            break
    else:
        print(Fore.RED + f"\n THE WORD IS {Wordle.upper()}.")

play_wordle()
