# console-based game
# computer will think of 3-digit number that has no repeating digits
# your goal is to guess that numbers
# the computer will give back clues
    # close - correct number but in the wrong position
    # match - correct number in the correct position
    # nope - none ot the guessed data matches results
# Keep doing it until you get a full match

# Try to figure out what this code is doing and how it might be useful to you
import random

# Opening message
print("Welcome to the 'Guess the Number' Game")
print("Enter 3-digit number and view results!")
print("Good luck!")

def generate_digits():  # returns list of ints
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def generate_guess():   # returns list of ints
    guess = input("What is your guess? ")
    return [int(s) for s in guess]

digits = generate_digits()

# print(digits)
# checking if a guess matches completedy the secret number
# input parameters are lists of integers
def check_match(guess, digits):
    for i in range(3):
        if guess[i] != digits[i]:
            return False
    return True

# checks if any of guessed integers are inside the secret number
# input parameters are lists of integers
def check_close(guess, digits):
    for g in guess:
        for d in digits:
            if d == g:
                return True
    return False

# Main game logic
def main():
    while True:
        guess = generate_guess()
        print(guess)
        if check_match(guess, digits):
            print("Congratulations, You've found the secret number!")
            print("It was {0} all the time!".format(digits))
            return True
        elif check_close(guess, digits):
            print("Close match!")
            print("One or more of your digits were correct")
        else:
            print("Nope, no guess!")

main()
