from random import randint

def numbers(number1, number2):
    return randint(number1, number2)

print("Welcome to the Basic Calculator!")
print("Enter two numbers to perform operations.")
print("Type 'q' to quit.\n")

while True:
    first_input = input("Give a number (or 'q' to quit): ")
    if first_input.lower() == 'q':
        print("Goodbye ")
        break

    second_input = input("Give another number (or 'q' to quit): ")
    if second_input.lower() == 'q':
        print("Goodbye ")
        break


    try:
        number1 = int(first_input)
        number2 = int(second_input)
    except ValueError:
        print(" One or both inputs were not valid integers.\n")
        continue


    
    print("\n Number Operations")
    print(f"Addition: {number1} + {number2} = {number1 + number2}")
    print(f"Subtraction: {number1} - {number2} = {number1 - number2}")
    print(f"Multiplication: {number1} * {number2} = {number1 * number2}")
    
    if number2 != 0:
        print(f"Division: {number1} / {number2} = {number1 / number2}")
    else:
        print("Cannot divide by zero.")

    print("\n---\n")
