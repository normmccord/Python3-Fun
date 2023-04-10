# Author: Norm McCord
# Date Created: 20230410
# Date Last Modified: 20230410
# Purpose: Using 'Random', the program will generate a random number and ask the user to guess it over and over again until the user guesses correctly
# References:
    # https://www.w3schools.com/python/module_random.asp
    # https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/


import random # loads the 'random' module

randomNumber = random.randint(1, 100) # the range is in the parenthesis (start, stop+1)
# print(randomNumber) # for debugging/testing

# w3schools shows that the 2nd number in the range is 'stop+1' but in my testing I have found that the 2nd number is, in fact, included.  This makes me think it's actually (start, stop).  Maybe one of us is wrong, or maybe I misinterpreted what they meant.
userGuess = None # establish a variable for the user's guess

print("I've thought of a random number between 1 and 100.  Let's see if you can guess it!")
# Guess the number
while userGuess != randomNumber: # until the random number and user guess are the same, run this loop
    # ask the user to guess the number
    userGuess = int(input("Guess: ")) # input is always a string in python, here it is converted to an int so it can be compared to the random number
    if userGuess == randomNumber:
        print("You guessed it!")
        break
    elif userGuess > randomNumber:
        print("Too high")
    else:
        print("Too low")
