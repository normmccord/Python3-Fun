# Author: Norm McCord
# Date Created: 20230410
# Date Last Modified: 20230410
# Purpose: An input validation library for numbers

# checks if input is a float
def isFloat(s):
    decimal_count = 0
    for i in s:
        if i == ".":
            decimal_count += 1
        elif not i.isdigit():
            return False
    if decimal_count <= 1:
        return True
    else:
        return False

# gets input and tests if float using isFloat
def getFloat():
    s = input("Enter a float: ")
    while not isFloat(s):
        print("Invalid input (", s, "): Try again")
        s = input("enter a float: ")
    return float(s)

# gets input and check if integer using isdigit
def getInt():
    s = input("Enter an int: ")
    while not s.isdigit():
        print("Invalid input (", s, "): Try again")
        s = input("enter an int: ")
    return int(s)
