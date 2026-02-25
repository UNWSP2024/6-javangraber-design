# Programmer: Javan Graber
# Date: 2/24/2026
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.

# First import the random module
import random

# Create a function that generates two random numbers and finds their sum
def randDice():
    # Generate the first number
    first_number = random.randint(1, 6)

    # Generate the second number
    second_number = random.randint(1, 6)

    # Find the sum of the two numbers
    sum_numbers = first_number + second_number

    # Return the sum to the calling function
    return sum_numbers

# Create the main function that simulates 100 rolls of the dice and calculates the
# average by calling for the randDice function and using the formula
def main():
    # Establish the total as starting at 0
    total = 0

    # Insert the for loop that calls the randDice function 100 times
    for dice_roll in range(100):
        sum_rolls = randDice()
        total = total + sum_rolls

    # Create the average formula
    average = total / 100

    # Print the average
    print(f'The average of the 100 rolls is {average:.2f}')

# Call the main function
main()
