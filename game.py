import random
import math

# Input the range
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Generate a random number between the lower and upper bounds
x = random.randint(lower, upper)

# Calculate the total number of chances based on the range
total_chances = math.ceil(math.log(upper - lower + 1, 2))

print(f"\n\tYou've only {total_chances} chances to guess the integer!\n")

count = 0  # Initialize the count for attempts
flag = False  # Flag to indicate if the user guessed correctly

# Loop for the guessing game
while count < total_chances:
    count += 1

    guess = int(input("Your guess number is: "))

    # Check the guess
    if guess == x:
        print(f"Congratulations! You did it in {count} tries.")
        flag = True
        break
    elif guess < x:
        print("The number you guessed is too low.")
    elif guess > x:
        print("The number you guessed is too high.")

# If the user fails to guess within the total chances
if not flag:
    print(f"\nThe correct number was {x}.")
    print("\tBetter luck next time!")
