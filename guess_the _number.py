from random import randint
def guess_number (start_number,end_number):
    user_number = randint(start_number,end_number)
    return user_number

computers_number= guess_number(1,100)

print("\n---\n")
print("\nLets play a game\n")
print("Guess a number between 1-100, lets try to guess the same number")
print("You have five tries to guess it.\n")

MAX_TRIES = 5

for attempt in range(1, MAX_TRIES + 1):
    try:
        users_number = int(input(f"Attempt {attempt}/{MAX_TRIES} — your guess: "))
    except ValueError:
        print("Please enter a valid whole number.\n")
        # Don’t count this as an attempt; let them try again
        continue

    if users_number == computers_number:
        print(f" Correct! You guessed it in {attempt} {'try' if attempt == 1 else 'tries'}.")
        break
    elif users_number > computers_number:
        print("Too high!\n")
    else:
        print("Too low!\n")
else:
    # This block runs if we never hit `break` (i.e. all tries used up)
    print(f" You’ve used all {MAX_TRIES} tries. You lose!")
    print(f"The number was: {computers_number}") 
