# Author: Norm McCord
# Date Created: 20230410
# Date Last Modified: 20230410
# Purpose: A program that generates a number between 1 and 66 (ie: 'rolls' a 6-sided dice).  It shows the user the result and asks if they want to roll again.
# References:
    # https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/

import random # the random module will be what generates the number ('rolls the dice')

f = "y" # this is to establsh a variable we can use inside the loop to continue or quit
while f == "y" or f == "Y": # "while" means this loop will continue 'while' f is equal to (==) y or Y (to account for the user entering a capital letter
    roll = int(random.randint(1, 6))
    print(roll)
    f = input("Roll again (y/n)? ")


