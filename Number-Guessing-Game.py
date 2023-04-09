# Author: Norm McCord
# Date Created: 20230404
# Date Last Modified: 20230404
# A number guessing game using a random number generator

import random

# 'randrange' takes a start number (included, optional) and a stop number (not included)
n = int(random.randrange(1, 101))
print("I'm thinking of a number between 1 and 100.  ")

not_it = True # this is a flag used to break the loop when the user guesses correctly
while not_it:
    user_guess = int(input("Guess: ")) # User guess prompt needs to be inside the loop so it keeps prompting if user is wrong.
    if user_guess == n:
        print("Got it!")
        not_it = False
        break
    elif user_guess > n:
        print("Too high")
    else:
        print("Too low")
